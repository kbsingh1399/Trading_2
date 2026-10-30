# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:39:17 IST` (`2026-10-30 10:09:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9240` | **Live Ask Quote**: `0.9440` | **Mid Price**: `0.9340`
- **Spread Points**: `20.00` | **Spread BPS**: `214.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.9100` | VWAP Z-Score: `+0.51` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0069` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.89` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9801` | Lower -3.00σ Band: `0.8399`
  * Upper +2.51σ Band: `0.9687` | Lower -2.51σ Band: `0.8514`
  * Upper +2.01σ Band: `0.9570` | Lower -2.01σ Band: `0.8630`
  * Upper +2.00σ Band: `0.9568` | Lower -2.00σ Band: `0.8633`
  * Upper +1.28σ Band: `0.9399` | Lower -1.28σ Band: `0.8801`
  * Upper +1.00σ Band: `0.9334` | Lower -1.00σ Band: `0.8866`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9276` | EMA-20=`0.9284` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9300` (Slope: `+0.0000`) | EMA-100=`0.9414`
  * Institutional Anchors: EMA-144=`0.9494` | EMA-200=`0.9573` (Slope: `-0.3452`) | EMA-233=`0.9604`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9447` (Distance: `-1.18%`)
  * Point of Control (POC) = `0.9119` (Distance: `+2.37%`)
  * Value Area Low (VAL) = `0.8998` (Distance: `+3.75%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9689`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9330` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9480` | Low=`0.9190`
  * New York Session (13:00-21:00 UTC): High=`0.9396` | Low=`0.9284`
  * Initial Balance (First Hour): IB High=`0.9480` | IB Low=`0.9290`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9303` - `0.9377`
  * Optimal Trade Entry (OTE 0.705): `0.9359`
  * Structural Invalidation Anchor (0.786): `0.9415`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9326` | `0.9330` | `0.9292` | `0.9329` | `216,409` | 201,419.57 USD | -71,651.88 USD | `-35.57%` | -5,838,714.35 USD | `-0.92` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9329` | `0.9344` | `0.9319` | `0.9342` | `75,001` | 69,991.25 USD | -20,547.27 USD | `-29.36%` | -5,859,261.62 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9342` | `0.9350` | `0.9329` | `0.9342` | `70,671` | 65,991.22 USD | -17,803.72 USD | `-26.98%` | -5,877,065.34 USD | `+0.67` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.9339` | `0.9366` | `0.9331` | `0.9363` | `291,787` | 272,828.10 USD | -28,574.65 USD | `-10.47%` | -5,669,647.15 USD | `+0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.9364` | `0.9364` | `0.9315` | `0.9328` | `346,655` | 323,640.65 USD | -97,415.33 USD | `-30.10%` | -5,767,062.47 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.9326` | `0.9350` | `0.9292` | `0.9342` | `362,080` | 337,402.04 USD | -110,002.87 USD | `-32.60%` | -5,877,065.34 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9521` | `0.9556` | `0.9420` | `0.9454` | `1,900,301` | 1,804,294.23 USD | -93,285.41 USD | `-5.17%` | -5,022,371.88 USD | `+0.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9454` | `0.9488` | `0.9359` | `0.9375` | `1,853,058` | 1,744,265.88 USD | -394,329.00 USD | `-22.61%` | -5,416,700.88 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.9375` | `0.9390` | `0.9292` | `0.9340` | `1,604,310` | 1,498,969.31 USD | -460,369.88 USD | `-30.71%` | -5,877,070.76 USD | `-0.17` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9340` | `3,457,369` | 3,243,235.19 USD | -854,698.88 USD | `-26.35%` | -5,770,597.84 USD | `+0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -974,642.25 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,499,370.98 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,092,983.65 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9603` | `0.9263` | `0.9454` | `10,832,060` | 10,247,507.62 USD | -822,915.31 USD | `-8.03%` | -4,915,898.96 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.9454` | `0.9488` | `0.9292` | `0.9340` | `3,457,369` | 3,243,235.19 USD | -854,698.88 USD | `-26.35%` | -5,770,597.84 USD | `+0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`0.9340`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `Live` | `Long Liquidation` | `0.1945` | 333.66 USD | 463,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2135` | 106.75 USD | 463,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 173.02 USD | 463,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3635` | 802.97 USD | 463,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,800.00 USD | 462,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4235` | 2,410.00 USD | 459,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 1,220.00 USD | 457,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4665` | 547.81 USD | 455,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 147.02 USD | 455,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 455,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5025` | 201.35 USD | 452,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 452,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5355` | 535.50 USD | 449,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 448,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 433,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 433,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 432,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5915` | 234.53 USD | 432,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 432,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6075` | 1,810.00 USD | 430,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 429,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 428,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6295` | 220.32 USD | 428,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 428,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 427,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 427,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 427,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 425,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 404,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 400,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 400,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 400,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6755` | 84,440.00 USD | 336,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 251,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 251,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6915` | 19,800.00 USD | 251,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 231,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 230,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7135` | 159.40 USD | 229,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 229,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 228,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 227,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7295` | 291.58 USD | 226,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 226,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 224,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 222,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7515` | 32,890.00 USD | 222,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 2,220.00 USD | 189,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,140.00 USD | 187,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 186,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7565` | 8,860.00 USD | 186,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7595` | 53,930.00 USD | 177,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 123,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7705` | 152.94 USD | 123,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 122,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7730` | 3,030,000.00 USD | 3,030,000.00 USD | 9,740.00 USD | 39.63 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7750` | 3,010,000.00 USD | 3,010,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 119,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7790` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7810` | 3,010,000.00 USD | 3,010,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7830` | 3,010,000.00 USD | 3,010,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7850` | 3,000,000.00 USD | 3,000,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 156.51 USD | 116,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7870` | 3,000,000.00 USD | 3,000,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,990,000.00 USD | 2,990,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 116,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 2,990,000.00 USD | 2,990,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 2,970,000.00 USD | 2,970,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7935` | 1,760.00 USD | 116,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7950` | 2,940,000.00 USD | 2,940,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 2,910,000.00 USD | 2,910,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7985` | 210.40 USD | 114,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7990` | 2,900,000.00 USD | 2,900,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 2,860,000.00 USD | 2,860,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 2,850,000.00 USD | 2,850,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 2,830,000.00 USD | 2,830,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 2,810,000.00 USD | 2,810,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 2,770,000.00 USD | 2,770,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 2,770,000.00 USD | 2,770,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 2,760,000.00 USD | 2,760,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 114,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 2,730,000.00 USD | 2,730,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 2,640,000.00 USD | 2,640,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 2,610,000.00 USD | 2,610,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 2,600,000.00 USD | 2,600,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 113,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8230` | 2,580,000.00 USD | 2,580,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 111,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8250` | 2,530,000.00 USD | 2,530,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 2,520,000.00 USD | 2,520,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 2,500,000.00 USD | 2,500,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 2,490,000.00 USD | 2,490,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 2,460,000.00 USD | 2,460,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 2,320,000.00 USD | 2,320,000.00 USD | 2,260.00 USD | 677.41 USD | 20,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 110,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 2,440,000.00 USD | 2,440,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 2,300,000.00 USD | 2,300,000.00 USD | 17,410.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 2,280,000.00 USD | 2,280,000.00 USD | 483.40 USD | 1,880.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 2,410,000.00 USD | 2,410,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 110,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,270,000.00 USD | 2,270,000.00 USD | 4,280.00 USD | 5,540.00 USD | 844.45 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 2,410,000.00 USD | 2,410,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,260,000.00 USD | 2,260,000.00 USD | 3,770.00 USD | 1,420.00 USD | 31.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 2,390,000.00 USD | 2,390,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,260,000.00 USD | 2,260,000.00 USD | 16,570.00 USD | 7,340.00 USD | 595.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 2,390,000.00 USD | 2,390,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,230,000.00 USD | 2,230,000.00 USD | 7,990.00 USD | 951.92 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 2,380,000.00 USD | 2,380,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 108,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,220,000.00 USD | 2,220,000.00 USD | 13,780.00 USD | 3,980.00 USD | 6,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 2,350,000.00 USD | 2,350,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 2,190,000.00 USD | 2,190,000.00 USD | 8,170.00 USD | 3,840.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 2,310,000.00 USD | 2,310,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,160,000.00 USD | 2,160,000.00 USD | 3,330.00 USD | 5,480.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 2,300,000.00 USD | 2,300,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,150,000.00 USD | 2,150,000.00 USD | 16,770.00 USD | 760.40 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 2,300,000.00 USD | 2,300,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 107,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,130,000.00 USD | 2,130,000.00 USD | 2,870.00 USD | 1,040.00 USD | 8,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 2,290,000.00 USD | 2,290,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,120,000.00 USD | 2,120,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 2,280,000.00 USD | 2,280,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,080,000.00 USD | 2,080,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 2,230,000.00 USD | 2,230,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 107,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,050,000.00 USD | 2,050,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 2,230,000.00 USD | 2,230,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 106,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 2,160,000.00 USD | 2,160,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,000,000.00 USD | 2,000,000.00 USD | 43,110.00 USD | 9,030.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 2,130,000.00 USD | 2,130,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 105,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,930,000.00 USD | 1,930,000.00 USD | 49,330.00 USD | 3,880.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8705` | 92,480.00 USD | 92,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,910,000.00 USD | 1,910,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,840,000.00 USD | 1,840,000.00 USD | 30,840.00 USD | 34,170.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,760,000.00 USD | 1,760,000.00 USD | 59,650.00 USD | 12,180.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,650,000.00 USD | 1,650,000.00 USD | 14,770.00 USD | 5,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,840,000.00 USD | 1,840,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 76.69 USD | 50,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,810,000.00 USD | 1,810,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,580,000.00 USD | 1,580,000.00 USD | 12,990.00 USD | 57.65 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,750,000.00 USD | 1,750,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,560,000.00 USD | 1,560,000.00 USD | 825.04 USD | 10,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,750,000.00 USD | 1,750,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,550,000.00 USD | 1,550,000.00 USD | 1,820.00 USD | 16,150.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,530,000.00 USD | 1,530,000.00 USD | 66,980.00 USD | 27,710.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,710,000.00 USD | 1,710,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 1,430,000.00 USD | 1,430,000.00 USD | 74,070.00 USD | 14,160.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,340,000.00 USD | 1,340,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 1,300,000.00 USD | 1,300,000.00 USD | 2,730.00 USD | 51,760.00 USD | 910.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,200,000.00 USD | 1,200,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 1,250,000.00 USD | 1,250,000.00 USD | 46,090.00 USD | 32,770.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.8925` | 665.36 USD | 665.36 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,060,000.00 USD | 1,060,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,110,000.00 USD | 1,110,000.00 USD | 16,380.00 USD | 18,130.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 968,550.00 USD | 968,550.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,080,000.00 USD | 1,080,000.00 USD | 5,530.00 USD | 28,510.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 866,340.00 USD | 866,340.00 USD | 2,140.00 USD | 4,820.00 USD | 56,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,040,000.00 USD | 1,040,000.00 USD | 4,780.00 USD | 27,590.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 803,050.00 USD | 803,050.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 984,040.00 USD | 984,040.00 USD | 8,600.00 USD | 17,350.00 USD | 2,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 768,830.00 USD | 768,830.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 955,100.00 USD | 955,100.00 USD | 4,110.00 USD | 11,830.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 719,990.00 USD | 719,990.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 936,140.00 USD | 936,140.00 USD | 12,290.00 USD | 22,810.00 USD | 28,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 679,690.00 USD | 679,690.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 872,280.00 USD | 872,280.00 USD | 30,140.00 USD | 10,280.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 675,850.00 USD | 675,850.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 806,750.00 USD | 806,750.00 USD | 20,470.00 USD | 10,040.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 756,730.00 USD | 756,730.00 USD | 8,170.00 USD | 3,480.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 743,370.00 USD | 743,370.00 USD | 32,330.00 USD | 5,580.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 609,900.00 USD | 609,900.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 702,520.00 USD | 702,520.00 USD | 9,600.00 USD | 14,360.00 USD | 31,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 589,180.00 USD | 589,180.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 647,500.00 USD | 647,500.00 USD | 9,260.00 USD | 8,060.00 USD | 18,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 572,980.00 USD | 572,980.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 611,880.00 USD | 611,880.00 USD | 14,340.00 USD | 9,170.00 USD | 14,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 574,240.00 USD | 574,240.00 USD | 8,570.00 USD | 11,210.00 USD | 5,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9210` | 539,800.00 USD | 539,800.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 548,730.00 USD | 548,730.00 USD | 13,740.00 USD | 3,470.00 USD | 877.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9230` | 528,070.00 USD | 528,070.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 530,640.00 USD | 530,640.00 USD | 88,170.00 USD | 20,790.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9250` | 207,020.00 USD | 207,020.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 378,100.00 USD | 378,100.00 USD | 35,300.00 USD | 51,770.00 USD | 83,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9270` | 70,170.00 USD | 70,170.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 207,400.00 USD | 207,400.00 USD | 92,240.00 USD | 12,420.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9290` | 14,350.00 USD | 14,350.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 36,190.00 USD | 36,190.00 USD | 5,140.00 USD | 15,160.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 12,050.00 USD | 12,050.00 USD | 0.00 USD | 7,510.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 68,810.00 USD | 68,810.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 137,630.00 USD | 137,630.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 47,780.00 USD | 47,780.00 USD | 3,720.00 USD | 17,650.00 USD | 26,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 169,150.00 USD | 169,150.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 85,460.00 USD | 85,460.00 USD | 36,510.00 USD | 321.19 USD | 852.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 253,550.00 USD | 253,550.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 85,570.00 USD | 85,570.00 USD | 0.00 USD | 103.28 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 327,710.00 USD | 327,710.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 88,130.00 USD | 88,130.00 USD | 2,020.00 USD | 548.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 490,760.00 USD | 490,760.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 89,360.00 USD | 89,360.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 89,590.00 USD | 89,590.00 USD | 0.00 USD | 224.96 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 515,050.00 USD | 515,050.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 89,870.00 USD | 89,870.00 USD | 0.00 USD | 199.60 USD | 79.38 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 601,560.00 USD | 601,560.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 91,840.00 USD | 91,840.00 USD | 1,790.00 USD | 0.00 USD | 176.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 685,500.00 USD | 685,500.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 177,200.00 USD | 177,200.00 USD | 85,280.00 USD | 85.68 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 976,890.00 USD | 976,890.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 185,620.00 USD | 185,620.00 USD | 0.00 USD | 5,520.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 985,130.00 USD | 985,130.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 219,710.00 USD | 219,710.00 USD | 17,510.00 USD | 9,220.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 274,950.00 USD | 274,950.00 USD | 25,050.00 USD | 24,220.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,020,000.00 USD | 1,020,000.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 293,820.00 USD | 293,820.00 USD | 7,260.00 USD | 9,120.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 1,040,000.00 USD | 1,040,000.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 321,740.00 USD | 321,740.00 USD | 17,180.00 USD | 8,190.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 1,060,000.00 USD | 1,060,000.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 483,740.00 USD | 483,740.00 USD | 81,730.00 USD | 20,070.00 USD | 60,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 1,240,000.00 USD | 1,240,000.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 661,240.00 USD | 661,240.00 USD | 53,800.00 USD | 43,860.00 USD | 79,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 1,350,000.00 USD | 1,350,000.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 728,670.00 USD | 728,670.00 USD | 16,900.00 USD | 13,350.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 1,390,000.00 USD | 1,390,000.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 797,390.00 USD | 797,390.00 USD | 46,820.00 USD | 17,940.00 USD | 3,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 871,930.00 USD | 871,930.00 USD | 16,500.00 USD | 13,730.00 USD | 44,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 985,470.00 USD | 985,470.00 USD | 35,560.00 USD | 9,270.00 USD | 68,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 1,530,000.00 USD | 1,530,000.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,060,000.00 USD | 1,060,000.00 USD | 32,970.00 USD | 9,760.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 1,600,000.00 USD | 1,600,000.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,160,000.00 USD | 1,160,000.00 USD | 55,080.00 USD | 27,390.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 1,700,000.00 USD | 1,700,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,230,000.00 USD | 1,230,000.00 USD | 44,310.00 USD | 4,920.00 USD | 18,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,310,000.00 USD | 1,310,000.00 USD | 38,340.00 USD | 11,420.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 1,910,000.00 USD | 1,910,000.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,390,000.00 USD | 1,390,000.00 USD | 32,680.00 USD | 21,970.00 USD | 24,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,150,000.00 USD | 2,150,000.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,480,000.00 USD | 1,480,000.00 USD | 13,910.00 USD | 16,870.00 USD | 58,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,570,000.00 USD | 1,570,000.00 USD | 59,170.00 USD | 7,150.00 USD | 26,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,280,000.00 USD | 2,280,000.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,610,000.00 USD | 1,610,000.00 USD | 17,200.00 USD | 3,710.00 USD | 17,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,300,000.00 USD | 2,300,000.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,720,000.00 USD | 1,720,000.00 USD | 66,490.00 USD | 7,820.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,340,000.00 USD | 2,340,000.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,770,000.00 USD | 1,770,000.00 USD | 12,690.00 USD | 5,030.00 USD | 31,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 3,940.00 USD | 4,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,800,000.00 USD | 1,800,000.00 USD | 25,690.00 USD | 1,250.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,500,000.00 USD | 2,500,000.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,830,000.00 USD | 1,830,000.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 2,600,000.00 USD | 2,600,000.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 1,910,000.00 USD | 1,910,000.00 USD | 54,550.00 USD | 10,770.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 852.22 USD | 5,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9990` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 49,260.00 USD | 18,230.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,660,000.00 USD | 2,660,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,010,000.00 USD | 2,010,000.00 USD | 16,910.00 USD | 2,030.00 USD | 7,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,810,000.00 USD | 2,810,000.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,040,000.00 USD | 2,040,000.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 2,860,000.00 USD | 2,860,000.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,180,000.00 USD | 2,180,000.00 USD | 103,670.00 USD | 10,200.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,920,000.00 USD | 2,920,000.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,240,000.00 USD | 2,240,000.00 USD | 23,240.00 USD | 9,330.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,950,000.00 USD | 2,950,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 2,990,000.00 USD | 2,990,000.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,310,000.00 USD | 2,310,000.00 USD | 16,880.00 USD | 15,730.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,040,000.00 USD | 3,040,000.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 7,030.00 USD | 5,790.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,380,000.00 USD | 2,380,000.00 USD | 9,410.00 USD | 22,350.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,120,000.00 USD | 3,120,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 26,110.00 USD | 1,160.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,240,000.00 USD | 3,240,000.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,480,000.00 USD | 2,480,000.00 USD | 33,560.00 USD | 9,540.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,400,000.00 USD | 3,400,000.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,540,000.00 USD | 2,540,000.00 USD | 25,690.00 USD | 15,810.00 USD | 25,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,710,000.00 USD | 3,710,000.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 42,800.00 USD | 8,420.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,830,000.00 USD | 3,830,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,690,000.00 USD | 2,690,000.00 USD | 34,170.00 USD | 19,050.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,140,000.00 USD | 4,140,000.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,730,000.00 USD | 2,730,000.00 USD | 16,260.00 USD | 8,440.00 USD | 14,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.03` | 152.32 USD | 5,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,350,000.00 USD | 4,350,000.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,830,000.00 USD | 2,830,000.00 USD | 65,530.00 USD | 13,320.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,550,000.00 USD | 4,550,000.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,900,000.00 USD | 2,900,000.00 USD | 31,870.00 USD | 8,470.00 USD | 32,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,680,000.00 USD | 4,680,000.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 13,500.00 USD | 9,390.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,990,000.00 USD | 4,990,000.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 2,960,000.00 USD | 2,960,000.00 USD | 4,560.00 USD | 11,000.00 USD | 6,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,300,000.00 USD | 5,300,000.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,020,000.00 USD | 3,020,000.00 USD | 45,570.00 USD | 3,700.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,680,000.00 USD | 5,680,000.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,050,000.00 USD | 3,050,000.00 USD | 9,270.00 USD | 6,500.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,130,000.00 USD | 6,130,000.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,070,000.00 USD | 3,070,000.00 USD | 12,480.00 USD | 7,160.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,320,000.00 USD | 6,320,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,090,000.00 USD | 3,090,000.00 USD | 3,380.00 USD | 1,840.00 USD | 11,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,590,000.00 USD | 6,590,000.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.05` | 3,100,000.00 USD | 3,100,000.00 USD | 4,070.00 USD | 4,930.00 USD | 844.60 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,110,000.00 USD | 7,110,000.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 5,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,320,000.00 USD | 7,320,000.00 USD | 112,190.00 USD | 13,780.00 USD | 77,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,630,000.00 USD | 7,630,000.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,830,000.00 USD | 7,830,000.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,060,000.00 USD | 8,060,000.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,460,000.00 USD | 8,460,000.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,910,000.00 USD | 8,910,000.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,190,000.00 USD | 9,190,000.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,470,000.00 USD | 9,470,000.00 USD | 140,500.00 USD | 73,690.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,670,000.00 USD | 9,670,000.00 USD | 74,870.00 USD | 27,820.00 USD | 91,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 9,750,000.00 USD | 9,750,000.00 USD | 60,290.00 USD | 26,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 8,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.15` | 13,750.00 USD | 22,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.31` | 126.85 USD | 22,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 33,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 34,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,900.00 USD | 38,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,200.00 USD | 41,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 122.39 USD | 41,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.42 USD | 41,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 43,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 795.79 USD | 44,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 2,440.00 USD | 46,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 240.59 USD | 46,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 55,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 55,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 621.35 USD | 56,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 322.10 USD | 56,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 56,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 13,140.00 USD | 69,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 380.81 USD | 70,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 89,340.00 USD | 159,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 159,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 24,030.00 USD | 183,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1945` | 463,720.00 USD | 0.00 USD | 333.66 USD | `-79.21%` | `1,715.50` |
| `Live` | `Long` | `0.2135` | 463,390.00 USD | 0.00 USD | 106.75 USD | `-77.18%` | `500.00` |
| `Live` | `Long` | `0.2735` | 463,280.00 USD | 0.00 USD | 173.02 USD | `-70.76%` | `632.60` |
| `Live` | `Long` | `0.3635` | 463,110.00 USD | 0.00 USD | 802.97 USD | `-61.14%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 462,300.00 USD | 0.00 USD | 2,800.00 USD | `-55.16%` | `6,675.20` |
| `Live` | `Long` | `0.4235` | 459,500.00 USD | 0.00 USD | 2,410.00 USD | `-54.73%` | `5,698.80` |
| `Live` | `Long` | `0.4645` | 457,090.00 USD | 0.00 USD | 1,220.00 USD | `-50.35%` | `2,618.10` |
| `Live` | `Long` | `0.4665` | 455,870.00 USD | 0.00 USD | 547.81 USD | `-50.13%` | `1,174.30` |
| `Live` | `Long` | `0.4685` | 455,330.00 USD | 0.00 USD | 147.02 USD | `-49.92%` | `313.80` |
| `Live` | `Long` | `0.4705` | 455,180.00 USD | 0.00 USD | 2,590.00 USD | `-49.71%` | `5,500.00` |
| `Live` | `Long` | `0.5025` | 452,590.00 USD | 0.00 USD | 201.35 USD | `-46.29%` | `400.70` |
| `Live` | `Long` | `0.5065` | 452,390.00 USD | 0.00 USD | 3,290.00 USD | `-45.86%` | `6,504.70` |
| `Live` | `Long` | `0.5355` | 449,100.00 USD | 0.00 USD | 535.50 USD | `-42.76%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 448,560.00 USD | 0.00 USD | 14,600.00 USD | `-39.55%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 433,960.00 USD | 0.00 USD | 577.36 USD | `-39.12%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 433,380.00 USD | 0.00 USD | 683.51 USD | `-37.52%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 432,700.00 USD | 0.00 USD | 137.53 USD | `-36.99%` | `233.30` |
| `Live` | `Long` | `0.5915` | 432,560.00 USD | 0.00 USD | 234.53 USD | `-36.77%` | `396.50` |
| `Live` | `Long` | `0.6055` | 432,330.00 USD | 0.00 USD | 1,480.00 USD | `-35.28%` | `2,448.50` |
| `Live` | `Long` | `0.6075` | 430,850.00 USD | 0.00 USD | 1,810.00 USD | `-35.06%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 429,040.00 USD | 0.00 USD | 105.96 USD | `-34.53%` | `173.00` |
| `Live` | `Long` | `0.6145` | 428,930.00 USD | 0.00 USD | 147.48 USD | `-34.31%` | `240.00` |
| `Live` | `Long` | `0.6295` | 428,790.00 USD | 0.00 USD | 220.32 USD | `-32.71%` | `350.00` |
| `Live` | `Long` | `0.6315` | 428,570.00 USD | 0.00 USD | 757.80 USD | `-32.50%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 427,810.00 USD | 0.00 USD | 106.00 USD | `-32.07%` | `166.80` |
| `Live` | `Long` | `0.6365` | 427,700.00 USD | 0.00 USD | 507.86 USD | `-31.96%` | `797.90` |
| `Live` | `Long` | `0.6405` | 427,190.00 USD | 0.00 USD | 2,090.00 USD | `-31.53%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 425,110.00 USD | 0.00 USD | 20,270.00 USD | `-31.43%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 404,840.00 USD | 0.00 USD | 4,230.00 USD | `-30.89%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 400,610.00 USD | 0.00 USD | 202.47 USD | `-30.79%` | `312.70` |
| `Live` | `Long` | `0.6595` | 400,410.00 USD | 0.00 USD | 149.44 USD | `-29.50%` | `226.60` |
| `Live` | `Long` | `0.6725` | 400,260.00 USD | 0.00 USD | 63,890.00 USD | `-28.11%` | `95,000.00` |
| `Live` | `Long` | `0.6755` | 336,370.00 USD | 0.00 USD | 84,440.00 USD | `-27.79%` | `125,000.00` |
| `Live` | `Long` | `0.6775` | 251,930.00 USD | 0.00 USD | 423.10 USD | `-27.58%` | `624.50` |
| `Live` | `Long` | `0.6835` | 251,510.00 USD | 0.00 USD | 512.97 USD | `-26.94%` | `750.50` |
| `Live` | `Long` | `0.6915` | 251,000.00 USD | 0.00 USD | 19,800.00 USD | `-26.08%` | `28,635.00` |
| `Live` | `Long` | `0.6965` | 231,190.00 USD | 0.00 USD | 322.62 USD | `-25.55%` | `463.20` |
| `Live` | `Long` | `0.7005` | 230,870.00 USD | 0.00 USD | 1,140.00 USD | `-25.12%` | `1,634.20` |
| `Live` | `Long` | `0.7135` | 229,730.00 USD | 0.00 USD | 159.40 USD | `-23.73%` | `223.40` |
| `Live` | `Long` | `0.7145` | 229,570.00 USD | 0.00 USD | 988.87 USD | `-23.62%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 228,580.00 USD | 0.00 USD | 1,580.00 USD | `-22.88%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 227,000.00 USD | 0.00 USD | 397.93 USD | `-22.66%` | `550.00` |
| `Live` | `Long` | `0.7295` | 226,600.00 USD | 0.00 USD | 291.58 USD | `-22.02%` | `399.70` |
| `Live` | `Long` | `0.7305` | 226,310.00 USD | 0.00 USD | 2,300.00 USD | `-21.91%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 224,010.00 USD | 0.00 USD | 1,140.00 USD | `-21.59%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 222,870.00 USD | 0.00 USD | 283.30 USD | `-20.95%` | `383.10` |
| `Live` | `Long` | `0.7515` | 222,590.00 USD | 0.00 USD | 32,890.00 USD | `-19.67%` | `43,766.90` |
| `Live` | `Long` | `0.7525` | 189,700.00 USD | 0.00 USD | 2,220.00 USD | `-19.56%` | `2,947.70` |
| `Live` | `Long` | `0.7535` | 187,480.00 USD | 0.00 USD | 1,140.00 USD | `-19.45%` | `1,516.30` |
| `Live` | `Long` | `0.7555` | 186,340.00 USD | 0.00 USD | 144.07 USD | `-19.24%` | `190.70` |
| `Live` | `Long` | `0.7565` | 186,190.00 USD | 0.00 USD | 8,860.00 USD | `-19.13%` | `11,712.10` |
| `Live` | `Long` | `0.7595` | 177,330.00 USD | 0.00 USD | 53,930.00 USD | `-18.81%` | `71,003.30` |
| `Live` | `Long` | `0.7635` | 123,400.00 USD | 0.00 USD | 308.00 USD | `-18.39%` | `403.40` |
| `Live` | `Long` | `0.7705` | 123,100.00 USD | 0.00 USD | 152.94 USD | `-17.64%` | `198.50` |
| `Live` | `Long` | `0.7725` | 122,940.00 USD | 0.00 USD | 3,840.00 USD | `-17.42%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 119,100.00 USD | 0.00 USD | 2,490.00 USD | `-16.89%` | `3,199.30` |
| `Live` | `Long` | `0.7865` | 116,620.00 USD | 0.00 USD | 156.51 USD | `-15.93%` | `199.00` |
| `Live` | `Long` | `0.7905` | 116,460.00 USD | 0.00 USD | 277.39 USD | `-15.50%` | `350.90` |
| `Live` | `Long` | `0.7935` | 116,180.00 USD | 0.00 USD | 1,760.00 USD | `-15.18%` | `2,214.10` |
| `Live` | `Long` | `0.7985` | 114,430.00 USD | 0.00 USD | 210.40 USD | `-14.64%` | `263.50` |
| `Live` | `Long` | `0.8135` | 114,220.00 USD | 0.00 USD | 647.79 USD | `-13.04%` | `796.30` |
| `Live` | `Long` | `0.8215` | 113,570.00 USD | 0.00 USD | 1,950.00 USD | `-12.19%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 111,620.00 USD | 0.00 USD | 749.96 USD | `-11.97%` | `910.70` |
| `Live` | `Long` | `0.8365` | 110,870.00 USD | 0.00 USD | 316.70 USD | `-10.58%` | `378.60` |
| `Live` | `Long` | `0.8415` | 110,550.00 USD | 0.00 USD | 1,570.00 USD | `-10.05%` | `1,862.40` |
| `Live` | `Long` | `0.8495` | 108,990.00 USD | 0.00 USD | 1,260.00 USD | `-9.19%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 107,720.00 USD | 0.00 USD | 620.32 USD | `-8.34%` | `723.40` |
| `Live` | `Long` | `0.8635` | 107,100.00 USD | 0.00 USD | 208.02 USD | `-7.70%` | `240.90` |
| `Live` | `Long` | `0.8645` | 106,900.00 USD | 0.00 USD | 438.30 USD | `-7.59%` | `507.00` |
| `Live` | `Long` | `0.8665` | 106,460.00 USD | 0.00 USD | 1,390.00 USD | `-7.38%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 105,070.00 USD | 0.00 USD | 12,590.00 USD | `-7.06%` | `14,478.80` |
| `Live` | `Long` | `0.8705` | 92,480.00 USD | 0.00 USD | 92,480.00 USD | `-6.95%` | `106,233.40` |
| `Live` | `Short` | `0.8925` | 665.36 USD | 665.36 USD | 0.00 USD | `-4.60%` | `745.50` |
| `Live` | `Short` | `0.9925` | 4,610.00 USD | 3,940.00 USD | 0.00 USD | `+6.09%` | `3,970.40` |
| `Live` | `Short` | `0.9985` | 5,460.00 USD | 852.22 USD | 0.00 USD | `+6.73%` | `853.50` |
| `Live` | `Short` | `1.03` | 5,610.00 USD | 152.32 USD | 0.00 USD | `+9.94%` | `148.10` |
| `Live` | `Short` | `1.05` | 5,980.00 USD | 367.04 USD | 0.00 USD | `+11.97%` | `350.40` |
| `Live` | `Short` | `1.08` | 8,210.00 USD | 2,230.00 USD | 0.00 USD | `+15.61%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 8,380.00 USD | 170.02 USD | 0.00 USD | `+18.71%` | `153.10` |
| `Live` | `Short` | `1.15` | 22,130.00 USD | 13,750.00 USD | 0.00 USD | `+22.77%` | `11,969.90` |
| `Live` | `Short` | `1.31` | 22,250.00 USD | 126.85 USD | 0.00 USD | `+40.51%` | `96.50` |
| `Live` | `Short` | `1.32` | 33,980.00 USD | 11,730.00 USD | 0.00 USD | `+41.48%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 34,220.00 USD | 239.77 USD | 0.00 USD | `+43.19%` | `179.00` |
| `Live` | `Short` | `1.38` | 38,120.00 USD | 3,900.00 USD | 0.00 USD | `+47.03%` | `2,834.10` |
| `Live` | `Short` | `1.42` | 41,320.00 USD | 3,200.00 USD | 0.00 USD | `+51.84%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 41,440.00 USD | 122.39 USD | 0.00 USD | `+64.56%` | `79.50` |
| `Live` | `Short` | `1.54` | 41,620.00 USD | 176.42 USD | 0.00 USD | `+64.99%` | `114.30` |
| `Live` | `Short` | `1.56` | 43,420.00 USD | 1,810.00 USD | 0.00 USD | `+66.38%` | `1,161.90` |
| `Live` | `Short` | `1.59` | 44,220.00 USD | 795.79 USD | 0.00 USD | `+70.34%` | `499.40` |
| `Live` | `Short` | `1.63` | 46,660.00 USD | 2,440.00 USD | 0.00 USD | `+73.76%` | `1,500.00` |
| `Live` | `Short` | `1.64` | 46,900.00 USD | 240.59 USD | 0.00 USD | `+75.79%` | `146.30` |
| `Live` | `Short` | `1.65` | 55,140.00 USD | 8,240.00 USD | 0.00 USD | `+76.11%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 55,440.00 USD | 300.15 USD | 0.00 USD | `+78.25%` | `180.00` |
| `Live` | `Short` | `1.68` | 56,060.00 USD | 621.35 USD | 0.00 USD | `+79.32%` | `370.40` |
| `Live` | `Short` | `1.68` | 56,380.00 USD | 322.10 USD | 0.00 USD | `+79.42%` | `191.90` |
| `Live` | `Short` | `1.73` | 56,570.00 USD | 190.42 USD | 0.00 USD | `+84.87%` | `110.10` |
| `Live` | `Short` | `1.74` | 69,710.00 USD | 13,140.00 USD | 0.00 USD | `+85.62%` | `7,569.10` |
| `Live` | `Short` | `1.77` | 70,100.00 USD | 380.81 USD | 0.00 USD | `+89.68%` | `214.60` |
| `Live` | `Short` | `1.80` | 159,440.00 USD | 89,340.00 USD | 0.00 USD | `+91.93%` | `49,759.80` |
| `Live` | `Short` | `1.86` | 159,650.00 USD | 208.37 USD | 0.00 USD | `+98.34%` | `112.30` |
| `Live` | `Short` | `1.86` | 183,680.00 USD | 24,030.00 USD | 0.00 USD | `+98.88%` | `12,916.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 357,000.00 USD | 0.00 USD | 120.45 USD | `-57.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 356,880.00 USD | 0.00 USD | 150.15 USD | `-46.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 356,730.00 USD | 0.00 USD | 186.15 USD | `-41.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 356,540.00 USD | 0.00 USD | 1,150.00 USD | `-30.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 355,390.00 USD | 0.00 USD | 781.90 USD | `-25.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 354,610.00 USD | 0.00 USD | 477.38 USD | `-24.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 354,130.00 USD | 0.00 USD | 341.33 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 353,790.00 USD | 0.00 USD | 972.82 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 352,820.00 USD | 0.00 USD | 160.20 USD | `-21.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 352,660.00 USD | 0.00 USD | 102.58 USD | `-21.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 352,560.00 USD | 0.00 USD | 289.49 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 352,270.00 USD | 0.00 USD | 197.53 USD | `-18.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 352,070.00 USD | 0.00 USD | 14,570.00 USD | `-16.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 337,500.00 USD | 0.00 USD | 213.58 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 337,290.00 USD | 0.00 USD | 274,830.00 USD | `-14.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 62,460.00 USD | 0.00 USD | 108.47 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8025` | 62,350.00 USD | 0.00 USD | 2,010.00 USD | `-14.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 60,330.00 USD | 0.00 USD | 326.96 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 60,010.00 USD | 0.00 USD | 405.75 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 59,600.00 USD | 0.00 USD | 772.84 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 58,830.00 USD | 0.00 USD | 2,670.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 56,160.00 USD | 0.00 USD | 3,470.00 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 52,690.00 USD | 0.00 USD | 9,180.00 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 43,510.00 USD | 0.00 USD | 341.94 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 43,160.00 USD | 0.00 USD | 1,150.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 42,020.00 USD | 0.00 USD | 429.25 USD | `-8.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 41,590.00 USD | 0.00 USD | 223.30 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 41,370.00 USD | 0.00 USD | 518.51 USD | `-7.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8675` | 40,850.00 USD | 0.00 USD | 128.39 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8705` | 40,720.00 USD | 0.00 USD | 1,280.00 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 39,440.00 USD | 0.00 USD | 205.24 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 39,230.00 USD | 0.00 USD | 649.66 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 38,580.00 USD | 0.00 USD | 194.06 USD | `-5.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 38,390.00 USD | 0.00 USD | 193.35 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 38,200.00 USD | 0.00 USD | 223.04 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 37,970.00 USD | 0.00 USD | 10,840.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 27,130.00 USD | 0.00 USD | 4,920.00 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 22,210.00 USD | 0.00 USD | 121.15 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 22,090.00 USD | 0.00 USD | 192.07 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 21,900.00 USD | 0.00 USD | 195.32 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 21,700.00 USD | 0.00 USD | 196.87 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 21,510.00 USD | 0.00 USD | 2,870.00 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 18,630.00 USD | 0.00 USD | 319.05 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 18,310.00 USD | 0.00 USD | 398.91 USD | `-3.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 17,920.00 USD | 0.00 USD | 196.96 USD | `-3.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 17,720.00 USD | 0.00 USD | 300.38 USD | `-3.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 17,420.00 USD | 0.00 USD | 198.61 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 17,220.00 USD | 0.00 USD | 994.35 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 16,220.00 USD | 0.00 USD | 363.40 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 15,860.00 USD | 0.00 USD | 1,810.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 14,060.00 USD | 0.00 USD | 397.23 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 13,660.00 USD | 0.00 USD | 398.65 USD | `-2.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 13,260.00 USD | 0.00 USD | 399.09 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 12,860.00 USD | 0.00 USD | 403.92 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 12,460.00 USD | 0.00 USD | 198.06 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 12,260.00 USD | 0.00 USD | 223.78 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 12,030.00 USD | 0.00 USD | 899.85 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 11,140.00 USD | 0.00 USD | 900.19 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 10,230.00 USD | 0.00 USD | 2,920.00 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 7,310.00 USD | 0.00 USD | 104.68 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 7,210.00 USD | 0.00 USD | 201.94 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9235` | 7,000.00 USD | 0.00 USD | 1,080.00 USD | `-1.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 5,920.00 USD | 0.00 USD | 201.45 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 5,720.00 USD | 0.00 USD | 817.40 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 4,900.00 USD | 0.00 USD | 403.77 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 4,500.00 USD | 0.00 USD | 2,120.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 2,380.00 USD | 0.00 USD | 246.05 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 2,130.00 USD | 0.00 USD | 407.49 USD | `-0.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9305` | 1,730.00 USD | 0.00 USD | 203.97 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9315` | 1,520.00 USD | 0.00 USD | 263.80 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9325` | 1,260.00 USD | 0.00 USD | 241.98 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9335` | 1,020.00 USD | 0.00 USD | 814.76 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9355` | 201.97 USD | 0.00 USD | 201.97 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 9,680.00 USD | 9,680.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 10,100.00 USD | 416.01 USD | 0.00 USD | `+0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 10,660.00 USD | 555.18 USD | 0.00 USD | `+0.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9415` | 11,650.00 USD | 997.80 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 12,470.00 USD | 816.96 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 12,800.00 USD | 334.28 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 40,220.00 USD | 27,420.00 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 40,600.00 USD | 383.87 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 41,230.00 USD | 623.93 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9475` | 70,160.00 USD | 28,930.00 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 70,570.00 USD | 414.68 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 70,960.00 USD | 381.00 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 72,970.00 USD | 2,020.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 76,770.00 USD | 3,790.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 77,000.00 USD | 236.26 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 77,140.00 USD | 136.83 USD | 0.00 USD | `+2.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 77,540.00 USD | 403.41 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 79,450.00 USD | 1,910.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 80,020.00 USD | 568.75 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 80,380.00 USD | 364.58 USD | 0.00 USD | `+3.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 81,210.00 USD | 824.91 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 81,590.00 USD | 385.74 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 83,630.00 USD | 2,030.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 83,890.00 USD | 262.52 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 84,280.00 USD | 387.83 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 85,110.00 USD | 830.10 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 107,070.00 USD | 21,960.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 107,470.00 USD | 396.17 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 108,140.00 USD | 676.53 USD | 0.00 USD | `+4.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 108,250.00 USD | 102.95 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 110,270.00 USD | 2,030.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 110,620.00 USD | 346.13 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 110,870.00 USD | 255.38 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 111,100.00 USD | 223.91 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 111,210.00 USD | 109.99 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 114,730.00 USD | 3,520.00 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 146,480.00 USD | 31,750.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 146,880.00 USD | 403.06 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 147,290.00 USD | 403.28 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 152,430.00 USD | 5,140.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 189,740.00 USD | 37,310.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 190,240.00 USD | 500.25 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 230,830.00 USD | 40,590.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 231,070.00 USD | 235.79 USD | 0.00 USD | `+7.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 232,410.00 USD | 1,340.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,640.00 USD | 230.39 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,770.00 USD | 127.65 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 232,990.00 USD | 218.64 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,400.00 USD | 409.86 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 233,510.00 USD | 110.95 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 234,130.00 USD | 615.60 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 234,690.00 USD | 561.17 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 234,900.00 USD | 214.40 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 235,150.00 USD | 249.88 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 235,360.00 USD | 207.97 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 235,570.00 USD | 208.26 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 236,080.00 USD | 516.75 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 236,430.00 USD | 348.86 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 236,820.00 USD | 391.80 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 237,240.00 USD | 413.76 USD | 0.00 USD | `+10.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 237,590.00 USD | 354.91 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 239,500.00 USD | 1,900.00 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 239,700.00 USD | 207.87 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 239,910.00 USD | 207.97 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 240,020.00 USD | 107.99 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 314,860.00 USD | 74,840.00 USD | 0.00 USD | `+13.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 317,030.00 USD | 2,170.00 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 318,570.00 USD | 1,540.00 USD | 0.00 USD | `+16.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 328,490.00 USD | 9,930.00 USD | 0.00 USD | `+17.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 329,370.00 USD | 877.63 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 329,540.00 USD | 171.09 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 332,310.00 USD | 2,770.00 USD | 0.00 USD | `+20.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 334,350.00 USD | 2,040.00 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 334,520.00 USD | 172.17 USD | 0.00 USD | `+20.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 334,690.00 USD | 172.32 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 334,880.00 USD | 187.72 USD | 0.00 USD | `+20.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 335,070.00 USD | 188.39 USD | 0.00 USD | `+21.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 337,740.00 USD | 2,670.00 USD | 0.00 USD | `+21.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 337,910.00 USD | 174.23 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 338,080.00 USD | 174.38 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 338,260.00 USD | 174.84 USD | 0.00 USD | `+21.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 338,410.00 USD | 150.90 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 338,560.00 USD | 151.03 USD | 0.00 USD | `+22.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 338,710.00 USD | 151.16 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 340,760.00 USD | 2,050.00 USD | 0.00 USD | `+24.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 340,870.00 USD | 110.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 341,350.00 USD | 475.80 USD | 0.00 USD | `+27.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 342,550.00 USD | 1,210.00 USD | 0.00 USD | `+28.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 385,480.00 USD | 42,930.00 USD | 0.00 USD | `+28.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 387,480.00 USD | 2,000.00 USD | 0.00 USD | `+31.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 388,870.00 USD | 1,380.00 USD | 0.00 USD | `+33.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 389,110.00 USD | 245.41 USD | 0.00 USD | `+36.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 397,510.00 USD | 8,390.00 USD | 0.00 USD | `+37.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 397,920.00 USD | 415.25 USD | 0.00 USD | `+39.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 404,440.00 USD | 6,520.00 USD | 0.00 USD | `+39.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 409,240.00 USD | 4,800.00 USD | 0.00 USD | `+40.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 409,890.00 USD | 655.75 USD | 0.00 USD | `+40.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 410,490.00 USD | 596.43 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 412,300.00 USD | 1,810.00 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 426,190.00 USD | 13,880.00 USD | 0.00 USD | `+43.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 427,440.00 USD | 1,250.00 USD | 0.00 USD | `+45.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 429,510.00 USD | 2,070.00 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 429,650.00 USD | 140.05 USD | 0.00 USD | `+49.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 429,810.00 USD | 160.42 USD | 0.00 USD | `+50.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 430,760.00 USD | 954.32 USD | 0.00 USD | `+50.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 464,930.00 USD | 34,170.00 USD | 0.00 USD | `+53.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 465,810.00 USD | 879.84 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 468,870.00 USD | 3,050.00 USD | 0.00 USD | `+62.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 469,170.00 USD | 297.27 USD | 0.00 USD | `+65.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 477,700.00 USD | 8,530.00 USD | 0.00 USD | `+76.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 477,840.00 USD | 143.99 USD | 0.00 USD | `+78.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 478,020.00 USD | 177.05 USD | 0.00 USD | `+89.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 478,450.00 USD | 431.40 USD | 0.00 USD | `+92.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 478,670.00 USD | 220.77 USD | 0.00 USD | `+94.39%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7730` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 9,740.00 USD | 39.63 USD | 2,230.00 USD |
| `7D` | `0.7750` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 698.40 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `0.7790` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7810` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 436.65 USD | 25.30 USD | 1,410.00 USD |
| `7D` | `0.7830` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 114.15 USD | 1,980.00 USD | 0.00 USD |
| `7D` | `0.7850` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 112.95 USD | 2,340.00 USD | 180.30 USD |
| `7D` | `0.7870` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 5,690.00 USD | 3,090.00 USD | 450.49 USD |
| `7D` | `0.7890` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 88.75 USD | 0.00 USD | 2,110.00 USD |
| `7D` | `0.7910` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 20,360.00 USD | 1,560.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 3,290.00 USD | 8,430.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 10,100.00 USD | 1,130.00 USD | 522.30 USD |
| `7D` | `0.7990` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 20,360.00 USD | 6,180.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 5,420.00 USD | 5,300.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 4,550.00 USD | 2,440.00 USD | 10,410.00 USD |
| `7D` | `0.8050` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 9,820.00 USD | 8,470.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 12,160.00 USD | 4,660.00 USD | 16,650.00 USD |
| `7D` | `0.8090` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 7,910.00 USD | 98.55 USD | 340.33 USD |
| `7D` | `0.8130` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 14,060.00 USD | 2,970.00 USD | 9,350.00 USD |
| `7D` | `0.8150` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 61,120.00 USD | 7,590.00 USD | 19,500.00 USD |
| `7D` | `0.8170` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 10,780.00 USD | 8,770.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 8,920.00 USD | 2,440.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 7,510.00 USD | 3,290.00 USD | 10,030.00 USD |
| `7D` | `0.8230` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 29,430.00 USD | 5,100.00 USD | 13,220.00 USD |
| `7D` | `0.8250` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 8,460.00 USD | 1,710.00 USD | 2,110.00 USD |
| `7D` | `0.8270` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 4,320.00 USD | 5,770.00 USD | 616.76 USD |
| `7D` | `0.8290` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 3,110.00 USD | 556.14 USD |
| `7D` | `0.8310` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 9,280.00 USD | 1,660.00 USD | 2,450.00 USD |
| `7D` | `0.8330` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 16,220.00 USD | 11,360.00 USD | 77.95 USD |
| `7D` | `0.8350` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8360` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 2,260.00 USD | 677.41 USD | 20,290.00 USD |
| `7D` | `0.8370` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 15,240.00 USD | 1,480.00 USD | 0.00 USD |
| `1D` | `0.8380` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 17,410.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8390` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8400` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 483.40 USD | 1,880.00 USD | 2,910.00 USD |
| `7D` | `0.8410` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 4,280.00 USD | 5,540.00 USD | 844.45 USD |
| `7D` | `0.8430` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 11,320.00 USD | 3,840.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 3,770.00 USD | 1,420.00 USD | 31.90 USD |
| `7D` | `0.8450` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,980.00 USD | 404.64 USD | 474.61 USD |
| `1D` | `0.8460` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 16,570.00 USD | 7,340.00 USD | 595.19 USD |
| `7D` | `0.8470` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 7,900.00 USD | 1,730.00 USD | 2,390.00 USD |
| `1D` | `0.8480` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 7,990.00 USD | 951.92 USD | 3,080.00 USD |
| `7D` | `0.8490` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 22,370.00 USD | 9,610.00 USD | 0.00 USD |
| `1D` | `0.8500` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 13,780.00 USD | 3,980.00 USD | 6,580.00 USD |
| `7D` | `0.8510` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 14,280.00 USD | 991.53 USD | 21,470.00 USD |
| `1D` | `0.8520` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 8,170.00 USD | 3,840.00 USD | 19,940.00 USD |
| `7D` | `0.8530` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 2,130.00 USD | 2,660.00 USD | 1,160.00 USD |
| `1D` | `0.8540` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 3,330.00 USD | 5,480.00 USD | 4,800.00 USD |
| `7D` | `0.8550` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 254.55 USD | 16.75 USD | 4,380.00 USD |
| `1D` | `0.8560` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 16,770.00 USD | 760.40 USD | 2,660.00 USD |
| `7D` | `0.8570` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 3,540.00 USD | 944.22 USD | 8,450.00 USD |
| `1D` | `0.8580` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 2,870.00 USD | 1,040.00 USD | 8,640.00 USD |
| `7D` | `0.8590` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 3,730.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.8600` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 7,990.00 USD | 10,610.00 USD | 18,580.00 USD |
| `7D` | `0.8610` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 9,960.00 USD | 3,660.00 USD | 35,340.00 USD |
| `1D` | `0.8620` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD |
| `7D` | `0.8630` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 758.91 USD | 2,910.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 47,860.00 USD | 18,930.00 USD | 184.85 USD |
| `1D` | `0.8660` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `0.8670` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 13,660.00 USD | 3,720.00 USD | 12,140.00 USD |
| `1D` | `0.8680` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 43,110.00 USD | 9,030.00 USD | 11,890.00 USD |
| `7D` | `0.8690` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 160,750.00 USD | 13,110.00 USD | 46,230.00 USD |
| `1D` | `0.8700` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 49,330.00 USD | 3,880.00 USD | 33,390.00 USD |
| `7D` | `0.8710` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 7,370.00 USD | 23,340.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 30,840.00 USD | 34,170.00 USD | 24,590.00 USD |
| `7D` | `0.8730` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 0.00 USD | 8,170.00 USD | 295.31 USD |
| `1D` | `0.8740` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 59,650.00 USD | 12,180.00 USD | 33,130.00 USD |
| `7D` | `0.8750` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 0.00 USD | 6,380.00 USD | 8,950.00 USD |
| `1D` | `0.8760` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 14,770.00 USD | 5,000.00 USD | 0.00 USD |
| `7D` | `0.8770` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,390.00 USD | 0.00 USD | 30,820.00 USD |
| `1D` | `0.8780` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 76.69 USD | 50,910.00 USD |
| `7D` | `0.8790` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 873.30 USD | 5,580.00 USD | 53,860.00 USD |
| `1D` | `0.8800` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 12,990.00 USD | 57.65 USD | 2,430.00 USD |
| `7D` | `0.8810` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 1,830.00 USD | 240.78 USD | 0.00 USD |
| `1D` | `0.8820` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 825.04 USD | 10,170.00 USD | 0.00 USD |
| `7D` | `0.8830` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 2,320.00 USD | 10,140.00 USD | 11,710.00 USD |
| `1D` | `0.8840` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,820.00 USD | 16,150.00 USD | 8,890.00 USD |
| `7D` | `0.8850` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 5,800.00 USD | 3,970.00 USD |
| `1D` | `0.8860` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 66,980.00 USD | 27,710.00 USD | 2,350.00 USD |
| `7D` | `0.8870` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 271,870.00 USD | 22,320.00 USD | 81,590.00 USD |
| `1D` | `0.8880` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 74,070.00 USD | 14,160.00 USD | 36,640.00 USD |
| `7D` | `0.8890` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 54,380.00 USD | 73,890.00 USD | 13,880.00 USD |
| `1D` | `0.8900` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 2,730.00 USD | 51,760.00 USD | 910.96 USD |
| `7D` | `0.8910` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 75,300.00 USD | 22,240.00 USD | 34,270.00 USD |
| `1D` | `0.8920` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 46,090.00 USD | 32,770.00 USD | 56,100.00 USD |
| `7D` | `0.8930` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 62,870.00 USD | 23,560.00 USD | 9,170.00 USD |
| `1D` | `0.8940` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 16,380.00 USD | 18,130.00 USD | 1,980.00 USD |
| `7D` | `0.8950` | 968,550.00 USD | 0.00 USD | 968,550.00 USD | 7,120.00 USD | 37,670.00 USD | 57,420.00 USD |
| `1D` | `0.8960` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 5,530.00 USD | 28,510.00 USD | 6,990.00 USD |
| `7D` | `0.8970` | 866,340.00 USD | 0.00 USD | 866,340.00 USD | 2,140.00 USD | 4,820.00 USD | 56,330.00 USD |
| `1D` | `0.8980` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 4,780.00 USD | 27,590.00 USD | 19,850.00 USD |
| `7D` | `0.8990` | 803,050.00 USD | 0.00 USD | 803,050.00 USD | 0.00 USD | 34,220.00 USD | 0.00 USD |
| `1D` | `0.9000` | 984,040.00 USD | 0.00 USD | 984,040.00 USD | 8,600.00 USD | 17,350.00 USD | 2,990.00 USD |
| `7D` | `0.9010` | 768,830.00 USD | 0.00 USD | 768,830.00 USD | 0.00 USD | 48,840.00 USD | 0.00 USD |
| `1D` | `0.9020` | 955,100.00 USD | 0.00 USD | 955,100.00 USD | 4,110.00 USD | 11,830.00 USD | 3,010.00 USD |
| `7D` | `0.9030` | 719,990.00 USD | 0.00 USD | 719,990.00 USD | 0.00 USD | 16,370.00 USD | 23,930.00 USD |
| `1D` | `0.9040` | 936,140.00 USD | 0.00 USD | 936,140.00 USD | 12,290.00 USD | 22,810.00 USD | 28,760.00 USD |
| `7D` | `0.9050` | 679,690.00 USD | 0.00 USD | 679,690.00 USD | 0.00 USD | 3,840.00 USD | 0.00 USD |
| `1D` | `0.9060` | 872,280.00 USD | 0.00 USD | 872,280.00 USD | 30,140.00 USD | 10,280.00 USD | 25,120.00 USD |
| `7D` | `0.9070` | 675,850.00 USD | 0.00 USD | 675,850.00 USD | 23,910.00 USD | 0.00 USD | 42,040.00 USD |
| `1D` | `0.9080` | 806,750.00 USD | 0.00 USD | 806,750.00 USD | 20,470.00 USD | 10,040.00 USD | 19,510.00 USD |
| `1D` | `0.9100` | 756,730.00 USD | 0.00 USD | 756,730.00 USD | 8,170.00 USD | 3,480.00 USD | 1,730.00 USD |
| `1D` | `0.9120` | 743,370.00 USD | 0.00 USD | 743,370.00 USD | 32,330.00 USD | 5,580.00 USD | 2,940.00 USD |
| `7D` | `0.9130` | 609,900.00 USD | 0.00 USD | 609,900.00 USD | 0.00 USD | 0.00 USD | 20,720.00 USD |
| `1D` | `0.9140` | 702,520.00 USD | 0.00 USD | 702,520.00 USD | 9,600.00 USD | 14,360.00 USD | 31,050.00 USD |
| `7D` | `0.9150` | 589,180.00 USD | 0.00 USD | 589,180.00 USD | 0.00 USD | 515.41 USD | 15,680.00 USD |
| `1D` | `0.9160` | 647,500.00 USD | 0.00 USD | 647,500.00 USD | 9,260.00 USD | 8,060.00 USD | 18,290.00 USD |
| `7D` | `0.9170` | 572,980.00 USD | 0.00 USD | 572,980.00 USD | 0.00 USD | 0.00 USD | 33,180.00 USD |
| `1D` | `0.9180` | 611,880.00 USD | 0.00 USD | 611,880.00 USD | 14,340.00 USD | 9,170.00 USD | 14,140.00 USD |
| `1D` | `0.9200` | 574,240.00 USD | 0.00 USD | 574,240.00 USD | 8,570.00 USD | 11,210.00 USD | 5,730.00 USD |
| `7D` | `0.9210` | 539,800.00 USD | 0.00 USD | 539,800.00 USD | 0.00 USD | 7,760.00 USD | 3,970.00 USD |
| `1D` | `0.9220` | 548,730.00 USD | 0.00 USD | 548,730.00 USD | 13,740.00 USD | 3,470.00 USD | 877.09 USD |
| `7D` | `0.9230` | 528,070.00 USD | 0.00 USD | 528,070.00 USD | 294,370.00 USD | 0.00 USD | 26,680.00 USD |
| `1D` | `0.9240` | 530,640.00 USD | 0.00 USD | 530,640.00 USD | 88,170.00 USD | 20,790.00 USD | 43,600.00 USD |
| `7D` | `0.9250` | 207,020.00 USD | 0.00 USD | 207,020.00 USD | 0.00 USD | 52,780.00 USD | 84,070.00 USD |
| `1D` | `0.9260` | 378,100.00 USD | 0.00 USD | 378,100.00 USD | 35,300.00 USD | 51,770.00 USD | 83,620.00 USD |
| `7D` | `0.9270` | 70,170.00 USD | 0.00 USD | 70,170.00 USD | 44,020.00 USD | 11,800.00 USD | 0.00 USD |
| `1D` | `0.9280` | 207,400.00 USD | 0.00 USD | 207,400.00 USD | 92,240.00 USD | 12,420.00 USD | 66,550.00 USD |
| `7D` | `0.9290` | 14,350.00 USD | 0.00 USD | 14,350.00 USD | 0.00 USD | 12,750.00 USD | 1,600.00 USD |
| `1D` | `0.9300` | 36,190.00 USD | 0.00 USD | 36,190.00 USD | 5,140.00 USD | 15,160.00 USD | 3,840.00 USD |
| `1D` | `0.9320` | 12,050.00 USD | 0.00 USD | 12,050.00 USD | 0.00 USD | 7,510.00 USD | 4,530.00 USD |
| `1D` | `0.9330` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9330` | 68,810.00 USD | 68,810.00 USD | 0.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `7D` | `0.9330` | 137,630.00 USD | 137,630.00 USD | 0.00 USD | 37,450.00 USD | 0.00 USD | 31,370.00 USD |
| `1D` | `0.9340` | 47,780.00 USD | 47,780.00 USD | 0.00 USD | 3,720.00 USD | 17,650.00 USD | 26,410.00 USD |
| `7D` | `0.9350` | 169,150.00 USD | 169,150.00 USD | 0.00 USD | 0.00 USD | 11,160.00 USD | 20,370.00 USD |
| `1D` | `0.9360` | 85,460.00 USD | 85,460.00 USD | 0.00 USD | 36,510.00 USD | 321.19 USD | 852.35 USD |
| `7D` | `0.9370` | 253,550.00 USD | 253,550.00 USD | 0.00 USD | 16,340.00 USD | 19,540.00 USD | 48,530.00 USD |
| `1D` | `0.9380` | 85,570.00 USD | 85,570.00 USD | 0.00 USD | 0.00 USD | 103.28 USD | 0.00 USD |
| `7D` | `0.9390` | 327,710.00 USD | 327,710.00 USD | 0.00 USD | 39,250.00 USD | 0.00 USD | 34,910.00 USD |
| `1D` | `0.9400` | 88,130.00 USD | 88,130.00 USD | 0.00 USD | 2,020.00 USD | 548.70 USD | 0.00 USD |
| `7D` | `0.9410` | 490,760.00 USD | 490,760.00 USD | 0.00 USD | 161,930.00 USD | 1,130.00 USD | 0.00 USD |
| `1D` | `0.9420` | 89,360.00 USD | 89,360.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9440` | 89,590.00 USD | 89,590.00 USD | 0.00 USD | 0.00 USD | 224.96 USD | 0.00 USD |
| `7D` | `0.9450` | 515,050.00 USD | 515,050.00 USD | 0.00 USD | 0.00 USD | 20,890.00 USD | 3,390.00 USD |
| `1D` | `0.9460` | 89,870.00 USD | 89,870.00 USD | 0.00 USD | 0.00 USD | 199.60 USD | 79.38 USD |
| `7D` | `0.9470` | 601,560.00 USD | 601,560.00 USD | 0.00 USD | 3,540.00 USD | 6,380.00 USD | 76,590.00 USD |
| `1D` | `0.9480` | 91,840.00 USD | 91,840.00 USD | 0.00 USD | 1,790.00 USD | 0.00 USD | 176.94 USD |
| `7D` | `0.9490` | 685,500.00 USD | 685,500.00 USD | 0.00 USD | 2,770.00 USD | 10,340.00 USD | 70,820.00 USD |
| `1D` | `0.9500` | 177,200.00 USD | 177,200.00 USD | 0.00 USD | 85,280.00 USD | 85.68 USD | 0.00 USD |
| `7D` | `0.9510` | 976,890.00 USD | 976,890.00 USD | 0.00 USD | 258,650.00 USD | 28,180.00 USD | 4,570.00 USD |
| `1D` | `0.9520` | 185,620.00 USD | 185,620.00 USD | 0.00 USD | 0.00 USD | 5,520.00 USD | 2,890.00 USD |
| `7D` | `0.9530` | 985,130.00 USD | 985,130.00 USD | 0.00 USD | 0.00 USD | 8,240.00 USD | 0.00 USD |
| `1D` | `0.9540` | 219,710.00 USD | 219,710.00 USD | 0.00 USD | 17,510.00 USD | 9,220.00 USD | 7,360.00 USD |
| `7D` | `0.9550` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 19,730.00 USD | 0.00 USD |
| `1D` | `0.9560` | 274,950.00 USD | 274,950.00 USD | 0.00 USD | 25,050.00 USD | 24,220.00 USD | 5,970.00 USD |
| `7D` | `0.9570` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 1,910.00 USD | 10,300.00 USD | 957.94 USD |
| `1D` | `0.9580` | 293,820.00 USD | 293,820.00 USD | 0.00 USD | 7,260.00 USD | 9,120.00 USD | 2,490.00 USD |
| `7D` | `0.9590` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 1,980.00 USD | 18,220.00 USD | 866.69 USD |
| `1D` | `0.9600` | 321,740.00 USD | 321,740.00 USD | 0.00 USD | 17,180.00 USD | 8,190.00 USD | 2,550.00 USD |
| `7D` | `0.9610` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 1,010.00 USD |
| `1D` | `0.9620` | 483,740.00 USD | 483,740.00 USD | 0.00 USD | 81,730.00 USD | 20,070.00 USD | 60,200.00 USD |
| `7D` | `0.9630` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 56,160.00 USD | 31,820.00 USD | 84,550.00 USD |
| `1D` | `0.9640` | 661,240.00 USD | 661,240.00 USD | 0.00 USD | 53,800.00 USD | 43,860.00 USD | 79,850.00 USD |
| `7D` | `0.9650` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 97,600.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9660` | 728,670.00 USD | 728,670.00 USD | 0.00 USD | 16,900.00 USD | 13,350.00 USD | 37,190.00 USD |
| `7D` | `0.9670` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 40,070.00 USD | 5,550.00 USD | 0.00 USD |
| `1D` | `0.9680` | 797,390.00 USD | 797,390.00 USD | 0.00 USD | 46,820.00 USD | 17,940.00 USD | 3,960.00 USD |
| `7D` | `0.9690` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 21,100.00 USD | 30,500.00 USD |
| `1D` | `0.9700` | 871,930.00 USD | 871,930.00 USD | 0.00 USD | 16,500.00 USD | 13,730.00 USD | 44,310.00 USD |
| `7D` | `0.9710` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 18,250.00 USD | 31,370.00 USD |
| `1D` | `0.9720` | 985,470.00 USD | 985,470.00 USD | 0.00 USD | 35,560.00 USD | 9,270.00 USD | 68,710.00 USD |
| `7D` | `0.9730` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 2,910.00 USD | 9,290.00 USD | 27,110.00 USD |
| `1D` | `0.9740` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 32,970.00 USD | 9,760.00 USD | 30,910.00 USD |
| `7D` | `0.9750` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 2,090.00 USD | 17,230.00 USD | 51,650.00 USD |
| `1D` | `0.9760` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 55,080.00 USD | 27,390.00 USD | 20,220.00 USD |
| `7D` | `0.9770` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 44,310.00 USD | 4,920.00 USD | 18,070.00 USD |
| `7D` | `0.9790` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | 85,420.00 USD |
| `1D` | `0.9800` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 38,340.00 USD | 11,420.00 USD | 31,120.00 USD |
| `7D` | `0.9810` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 540.00 USD | 4,020.00 USD | 119,460.00 USD |
| `1D` | `0.9820` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 32,680.00 USD | 21,970.00 USD | 24,670.00 USD |
| `7D` | `0.9830` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 124,720.00 USD | 15,810.00 USD | 94,290.00 USD |
| `1D` | `0.9840` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 13,910.00 USD | 16,870.00 USD | 58,220.00 USD |
| `7D` | `0.9850` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 59,170.00 USD | 7,150.00 USD | 26,140.00 USD |
| `7D` | `0.9870` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,950.00 USD |
| `1D` | `0.9880` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 17,200.00 USD | 3,710.00 USD | 17,030.00 USD |
| `7D` | `0.9890` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `0.9900` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 66,490.00 USD | 7,820.00 USD | 33,010.00 USD |
| `7D` | `0.9910` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 3,700.00 USD | 800.44 USD | 35,270.00 USD |
| `1D` | `0.9920` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 12,690.00 USD | 5,030.00 USD | 31,930.00 USD |
| `7D` | `0.9930` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 36,000.00 USD |
| `1D` | `0.9940` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 25,690.00 USD | 1,250.00 USD | 10,030.00 USD |
| `7D` | `0.9950` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 63,060.00 USD | 5,380.00 USD | 58,050.00 USD |
| `1D` | `0.9960` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 19,070.00 USD | 3,600.00 USD | 7,450.00 USD |
| `7D` | `0.9970` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 95,130.00 USD | 253.35 USD | 4,670.00 USD |
| `1D` | `0.9980` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 54,550.00 USD | 10,770.00 USD | 15,870.00 USD |
| `7D` | `0.9990` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 462.12 USD |
| `1D` | `1.00` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 49,260.00 USD | 18,230.00 USD | 6,740.00 USD |
| `7D` | `1.00` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 16,910.00 USD | 2,030.00 USD | 7,260.00 USD |
| `7D` | `1.00` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 107,670.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 10,790.00 USD | 9,550.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 12,730.00 USD |
| `1D` | `1.01` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 103,670.00 USD | 10,200.00 USD | 23,260.00 USD |
| `7D` | `1.01` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 35,710.00 USD | 240.78 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 23,240.00 USD | 9,330.00 USD | 30,960.00 USD |
| `7D` | `1.01` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD |
| `7D` | `1.01` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 20,090.00 USD | 17,980.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 16,880.00 USD | 15,730.00 USD | 265.91 USD |
| `7D` | `1.01` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 16,020.00 USD | 34,930.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 7,030.00 USD | 5,790.00 USD | 15,870.00 USD |
| `7D` | `1.01` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 26,510.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 9,410.00 USD | 22,350.00 USD | 9,680.00 USD |
| `7D` | `1.02` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 26,110.00 USD | 1,160.00 USD | 9,230.00 USD |
| `7D` | `1.02` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 17,960.00 USD | 83,360.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 33,560.00 USD | 9,540.00 USD | 18,280.00 USD |
| `7D` | `1.02` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 61,450.00 USD | 32,840.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 25,690.00 USD | 15,810.00 USD | 25,390.00 USD |
| `7D` | `1.02` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 82,230.00 USD | 86,210.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 42,800.00 USD | 8,420.00 USD | 29,040.00 USD |
| `7D` | `1.02` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 34,170.00 USD | 19,050.00 USD | 16,660.00 USD |
| `7D` | `1.03` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 161,070.00 USD | 127,000.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 16,260.00 USD | 8,440.00 USD | 14,610.00 USD |
| `7D` | `1.03` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 142,240.00 USD | 38,860.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 65,530.00 USD | 13,320.00 USD | 18,360.00 USD |
| `7D` | `1.03` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 170,960.00 USD | 10,970.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 31,870.00 USD | 8,470.00 USD | 32,160.00 USD |
| `7D` | `1.03` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 122,910.00 USD | 95.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 13,500.00 USD | 9,390.00 USD | 13,550.00 USD |
| `7D` | `1.03` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 259,060.00 USD | 8,290.00 USD | 43,700.00 USD |
| `1D` | `1.04` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 4,560.00 USD | 11,000.00 USD | 6,050.00 USD |
| `7D` | `1.04` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 193,150.00 USD | 3,330.00 USD | 109,460.00 USD |
| `1D` | `1.04` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 45,570.00 USD | 3,700.00 USD | 8,740.00 USD |
| `7D` | `1.04` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 239,580.00 USD | 9,010.00 USD | 134,440.00 USD |
| `1D` | `1.04` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 9,270.00 USD | 6,500.00 USD | 16,260.00 USD |
| `7D` | `1.04` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 285,690.00 USD | 2,090.00 USD | 159,500.00 USD |
| `1D` | `1.04` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 12,480.00 USD | 7,160.00 USD | 3,380.00 USD |
| `7D` | `1.04` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `1D` | `1.04` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 3,380.00 USD | 1,840.00 USD | 11,150.00 USD |
| `7D` | `1.04` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 184,670.00 USD | 23,770.00 USD | 59,810.00 USD |
| `1D` | `1.05` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 4,070.00 USD | 4,930.00 USD | 844.60 USD |
| `7D` | `1.05` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 178,890.00 USD | 96,370.00 USD | 244,850.00 USD |
| `7D` | `1.05` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 112,190.00 USD | 13,780.00 USD | 77,620.00 USD |
| `7D` | `1.05` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 175,350.00 USD | 43,690.00 USD | 96,730.00 USD |
| `7D` | `1.05` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 68,010.00 USD | 58,070.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 121,450.00 USD | 33,860.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 218,860.00 USD | 70,160.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 239,650.00 USD | 74,380.00 USD | 145,170.00 USD |
| `7D` | `1.06` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 138,520.00 USD | 56,310.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 140,500.00 USD | 73,690.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 9,670,000.00 USD | 9,670,000.00 USD | 0.00 USD | 74,870.00 USD | 27,820.00 USD | 91,220.00 USD |
| `7D` | `1.07` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 60,290.00 USD | 26,450.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `172.18M` | Total OI Tokens: `184,606,594.3 DOT`
  * 1h OI Change: `-0.72%` | 4h OI Change: `-2.00%` | 24h OI Change: `-17.18%`
  * Exchange Breakdown: Binance=`33.75M` | Bybit=`22.01M` | OKX=`9.94M` | Hyperliquid=`5.79M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.63K` | Last 24h: `6.26K` | Last 3d: `-7.35K` | Last 7d: `-25.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0101%` |
| **USDT Bybit** | `0.0026%` | **USDT KuCoin** | `-0.0168%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0055%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `51.94%` | `48.06%` | `1.08` | 22,260,000.00 USD |
| `15M` | `Binance` | `54.08%` | `45.92%` | `1.18` | 6,690,000.00 USD |
| `15M` | `OKX` | `50.25%` | `49.75%` | `1.01` | 2,390,000.00 USD |
| `15M` | `Bybit` | `38.28%` | `61.72%` | `0.62` | 4,280,000.00 USD |
| `15M` | `KuCoin` | `68.35%` | `31.65%` | `2.16` | 179,260.00 USD |
| `15M` | `Gate` | `56.15%` | `43.85%` | `1.28` | 287,670.00 USD |
| `15M` | `Bitget` | `58.94%` | `41.06%` | `1.44` | 548,850.00 USD |
| `15M` | `BingX` | `62.01%` | `37.99%` | `1.63` | 1,500,000.00 USD |
| `15M` | `MEXC` | `32.92%` | `67.08%` | `0.49` | 512,560.00 USD |
| `15M` | `Bitunix` | `46.38%` | `53.62%` | `0.86` | 485,200.00 USD |
| `15M` | `Hyperliquid` | `70.37%` | `29.63%` | `2.37` | 3,720,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.09%` | `50.91%` | `0.96` | 84,020.00 USD |
| `15M` | `Crypto.com` | `41.04%` | `58.96%` | `0.70` | 1,170.00 USD |
| `15M` | `WhiteBIT` | `25.82%` | `74.18%` | `0.35` | 1,120,000.00 USD |
| `15M` | `HTX` | `37.36%` | `62.64%` | `0.60` | 14,270.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `47.32%` | `52.68%` | `0.90` | 329,670.00 USD |
| `15M` | `Aster` | `29.41%` | `70.59%` | `0.42` | 37,110.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `63.18%` | `36.82%` | `1.72` | 86,540.00 USD |
| `15M` | `Whale Positions` | `54.08%` | `45.92%` | `1.18` | 6,690,000.00 USD |
| `15M` | `Global Accounts` | `51.94%` | `48.06%` | `1.08` | 22,260,000.00 USD |
| `1H` | `DOT` | `51.52%` | `48.48%` | `1.06` | 20,910,000.00 USD |
| `1H` | `Binance` | `48.09%` | `51.91%` | `0.93` | 7,530,000.00 USD |
| `1H` | `OKX` | `50.33%` | `49.67%` | `1.01` | 4,150,000.00 USD |
| `1H` | `Bybit` | `52.42%` | `47.58%` | `1.10` | 1,230,000.00 USD |
| `1H` | `KuCoin` | `52.15%` | `47.85%` | `1.09` | 319,460.00 USD |
| `1H` | `Gate` | `54.73%` | `45.27%` | `1.21` | 572,820.00 USD |
| `1H` | `Bitget` | `47.09%` | `52.91%` | `0.89` | 957,340.00 USD |
| `1H` | `BingX` | `27.69%` | `72.31%` | `0.38` | 1,090,000.00 USD |
| `1H` | `MEXC` | `60.02%` | `39.98%` | `1.50` | 2,230,000.00 USD |
| `1H` | `Bitunix` | `49.17%` | `50.83%` | `0.97` | 850,930.00 USD |
| `1H` | `Hyperliquid` | `49.01%` | `50.99%` | `0.96` | 264,800.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.58%` | `58.42%` | `0.71` | 220,550.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `85.48%` | `14.52%` | `5.89` | 1,350,000.00 USD |
| `1H` | `HTX` | `35.71%` | `64.29%` | `0.56` | 22,180.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.47%` | `55.53%` | `0.80` | 80,820.00 USD |
| `1H` | `Aster` | `78.33%` | `21.67%` | `3.61` | 9,020.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `9.14%` | `90.86%` | `0.10` | 29,150.00 USD |
| `1H` | `Whale Positions` | `48.09%` | `51.91%` | `0.93` | 7,530,000.00 USD |
| `1H` | `Global Accounts` | `51.52%` | `48.48%` | `1.06` | 20,910,000.00 USD |
| `4H` | `DOT` | `44.03%` | `55.97%` | `0.79` | 101,290,000.00 USD |
| `4H` | `Binance` | `49.63%` | `50.37%` | `0.99` | 38,000,000.00 USD |
| `4H` | `OKX` | `48.47%` | `51.53%` | `0.94` | 14,060,000.00 USD |
| `4H` | `Bybit` | `45.28%` | `54.72%` | `0.83` | 8,530,000.00 USD |
| `4H` | `KuCoin` | `53.53%` | `46.47%` | `1.15` | 1,330,000.00 USD |
| `4H` | `Gate` | `54.56%` | `45.44%` | `1.20` | 2,930,000.00 USD |
| `4H` | `Bitget` | `34.62%` | `65.38%` | `0.53` | 4,790,000.00 USD |
| `4H` | `BingX` | `36.75%` | `63.25%` | `0.58` | 5,310,000.00 USD |
| `4H` | `MEXC` | `49.97%` | `50.03%` | `1.00` | 14,760,000.00 USD |
| `4H` | `Bitunix` | `48.05%` | `51.95%` | `0.92` | 3,270,000.00 USD |
| `4H` | `Hyperliquid` | `30.18%` | `69.82%` | `0.43` | 1,500,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.64%` | `49.36%` | `1.03` | 2,080,000.00 USD |
| `4H` | `Crypto.com` | `40.02%` | `59.98%` | `0.67` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.83%` | `87.17%` | `0.15` | 3,990,000.00 USD |
| `4H` | `HTX` | `49.32%` | `50.68%` | `0.97` | 245,900.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `17.59%` | `82.41%` | `0.21` | 239,670.00 USD |
| `4H` | `Aster` | `11.1%` | `88.9%` | `0.12` | 156,970.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.79%` | `59.21%` | `0.69` | 111,320.00 USD |
| `4H` | `Whale Positions` | `49.63%` | `50.37%` | `0.99` | 38,000,000.00 USD |
| `4H` | `Global Accounts` | `44.03%` | `55.97%` | `0.79` | 101,290,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9436` | `0.9445` | `0.9436` | `0.9473` | `0.9425` | 430,563.34 USD | 161,800.40 USD | 268,762.94 USD | -106,962.53 USD | `-24.84%` | `2B / 14S` |
| `0:00 UTC` | `0.9446` | `0.9460` | `0.9446` | `0.9486` | `0.9442` | 368,731.69 USD | 177,970.36 USD | 190,761.33 USD | -12,790.97 USD | `-3.47%` | `10B / 4S` |
| `5:00 UTC` | `0.9438` | `0.9447` | `0.9438` | `0.9488` | `0.9423` | 353,543.62 USD | 111,318.38 USD | 242,225.25 USD | -130,906.87 USD | `-37.03%` | `2B / 19S` |
| `0:00 UTC` | `0.9378` | `0.9391` | `0.9378` | `0.9427` | `0.9366` | 674,681.66 USD | 251,815.20 USD | 422,866.46 USD | -171,051.26 USD | `-25.35%` | `2B / 15S` |
| `5:00 UTC` | `0.9365` | `0.9373` | `0.9365` | `0.9404` | `0.9360` | 347,308.90 USD | 133,864.50 USD | 213,444.40 USD | -79,579.90 USD | `-22.91%` | `8B / 13S` |
| `0:00 UTC` | `0.9349` | `0.9360` | `0.9349` | `0.9390` | `0.9338` | 565,103.94 USD | 170,366.16 USD | 394,737.78 USD | -224,371.62 USD | `-39.70%` | `1B / 22S` |
| `5:00 UTC` | `0.9357` | `0.9351` | `0.9357` | `0.9366` | `0.9332` | 272,828.10 USD | 122,126.72 USD | 150,701.37 USD | -28,574.65 USD | `-10.47%` | `1B / 6S` |
| `0:00 UTC` | `0.9343` | `0.9337` | `0.9343` | `0.9365` | `0.9315` | 323,640.65 USD | 113,112.66 USD | 210,527.99 USD | -97,415.33 USD | `-30.10%` | `2B / 14S` |
| `5:00 UTC` | `0.9312` | `0.9319` | `0.9312` | `0.9351` | `0.9293` | 338,159.00 USD | 113,706.78 USD | 224,452.22 USD | -110,745.44 USD | `-32.75%` | `4B / 15S` |
| `0:00 UTC` | `0.9328` | `0.9332` | `0.9328` | `0.9345` | `0.9322` | 233,219.37 USD | 102,170.84 USD | 131,048.53 USD | -28,877.69 USD | `-12.38%` | `2B / 3S` |

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
| `5m` | -3,860.00 USD | -16,420.00 USD | **`DISTRIBUTION`** |
| `15m` | 13,770.00 USD | -162,810.00 USD | **`DISTRIBUTION`** |
| `30m` | 53,080.00 USD | -305,980.00 USD | **`DISTRIBUTION`** |
| `1h` | -60,230.00 USD | -626,060.00 USD | **`DISTRIBUTION`** |
| `2h` | -102,390.00 USD | -1,190,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -294,150.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -192,550.00 USD | -2,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -75,780.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `12h` | -314,940.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,450,000.00 USD | -9,490,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,090,000.00 USD | -24,500,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,830,000.00 USD | -79,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.86K` | 15m=`+13.77K` | 1h=`-60.23K` | 24h=`-1.45M`
* Futures Capital Netflows: 5m=`-16.42K` | 15m=`-162.81K` | 1h=`-626.06K` | 24h=`-9.49M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8998` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8615` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.9998`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9447` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9830` (Risk Distance: `0.0400` pts)
  * +2.5R Take Profit: `0.8447`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9415`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
