# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:31:46 IST` (`2026-10-30 05:01:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9290` | **Live Ask Quote**: `0.9500` | **Mid Price**: `0.9395`
- **Spread Points**: `21.00` | **Spread BPS**: `223.52 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.8942` | VWAP Z-Score: `+1.94` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0093` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `57.32` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9403` | Lower -3.00σ Band: `0.8482`
  * Upper +2.51σ Band: `0.9328` | Lower -2.51σ Band: `0.8557`
  * Upper +2.01σ Band: `0.9251` | Lower -2.01σ Band: `0.8634`
  * Upper +2.00σ Band: `0.9249` | Lower -2.00σ Band: `0.8635`
  * Upper +1.28σ Band: `0.9139` | Lower -1.28σ Band: `0.8746`
  * Upper +1.00σ Band: `0.9096` | Lower -1.00σ Band: `0.8789`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9161` | EMA-20=`0.9128` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9268` (Slope: `+0.0000`) | EMA-100=`0.9454`
  * Institutional Anchors: EMA-144=`0.9544` | EMA-200=`0.9614` (Slope: `-0.6462`) | EMA-233=`0.9655`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9253` (Distance: `+1.59%`)
  * Point of Control (POC) = `0.9110` (Distance: `+3.18%`)
  * Value Area Low (VAL) = `0.8938` (Distance: `+5.17%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9310` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9433` | Low=`0.9357`
  * New York Session (13:00-21:00 UTC): High=`0.9451` | Low=`0.9339`
  * Initial Balance (First Hour): IB High=`0.9423` | IB Low=`0.9367`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9357` - `0.9433`
  * Optimal Trade Entry (OTE 0.705): `0.9414`
  * Structural Invalidation Anchor (0.786): `0.9470`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9341` | `0.9359` | `0.9332` | `0.9351` | `148,224` | 138,552.59 USD | 8,284.90 USD | `+5.98%` | -4,000,386.00 USD | `+0.10` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.9351` | `0.9356` | `0.9339` | `0.9348` | `124,967` | 116,794.07 USD | 19,984.13 USD | `+17.11%` | -3,980,401.88 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9347` | `0.9352` | `0.9333` | `0.9351` | `77,752` | 72,636.68 USD | 1,783.70 USD | `+2.46%` | -3,978,618.18 USD | `+0.05` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9308` | `0.9343` | `0.9288` | `0.9342` | `533,766` | 497,143.85 USD | 29,318.60 USD | `+5.90%` | -3,843,507.06 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9341` | `0.9365` | `0.9332` | `0.9361` | `432,462` | 404,247.05 USD | 41,914.22 USD | `+10.37%` | -3,801,592.84 USD | `-0.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9361` | `0.9428` | `0.9361` | `0.9417` | `983,571` | 924,579.99 USD | -56,242.08 USD | `-6.08%` | -3,857,834.92 USD | `-0.24` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9068` | `0.9231` | `0.9022` | `0.9175` | `3,555,217` | 3,250,542.04 USD | 108,464.97 USD | `+3.34%` | -3,777,368.70 USD | `+0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9176` | `0.9341` | `0.9170` | `0.9318` | `3,070,214` | 2,839,814.60 USD | -92,909.79 USD | `-3.27%` | -3,870,278.49 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9318` | `0.9428` | `0.9263` | `0.9416` | `2,514,965` | 2,351,059.36 USD | 12,025.83 USD | `+0.51%` | -3,858,252.66 USD | `+0.22` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9359` | `0.9263` | `0.9351` | `1,450,319` | 1,350,633.41 USD | 56,824.16 USD | `+4.21%` | -3,951,095.09 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -92,512.40 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -889,577.85 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9428` | `0.9263` | `0.9417` | `2,515,664` | 2,351,717.89 USD | 12,684.36 USD | `+0.54%` | -3,995,234.88 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.9734` | 545.61 USD | `-` | `NEWS_INTEL` | `-` | #DOT Liquidated Short: 0.55K USD at 0.9734 USD [API] | `2026-10-29 01:59:46` |


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
| `Live` | `Long Liquidation` | `0.2135` | 366.26 USD | 441,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 113.75 USD | 441,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3615` | 798.55 USD | 440,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,800.00 USD | 440,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4275` | 2,440.00 USD | 437,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 315.16 USD | 434,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4675` | 146.70 USD | 434,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 434,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4915` | 1,290.00 USD | 431,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 430,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5405` | 540.50 USD | 427,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5645` | 223.82 USD | 426,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 426,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 411,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5785` | 151.62 USD | 411,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 411,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 410,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 410,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 408,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 407,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 406,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6165` | 247.03 USD | 406,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 406,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 405,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 405,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 405,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 403,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 382,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 378,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 378,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 378,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 314,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6805` | 85,060.00 USD | 313,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 228,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 478.22 USD | 228,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6985` | 20,000.00 USD | 227,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 207,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 206,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 205,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 204,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 203,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 201,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 200,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 199,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 199,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 8,990.00 USD | 198,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 54,070.00 USD | 189,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 134,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7700` | 3,030,000.00 USD | 3,030,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7720` | 3,020,000.00 USD | 3,020,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 134,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7740` | 3,010,000.00 USD | 3,010,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7760` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 130,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 128,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 3,000,000.00 USD | 3,000,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7820` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7840` | 3,000,000.00 USD | 3,000,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 128,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7880` | 2,990,000.00 USD | 2,990,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 2,990,000.00 USD | 2,990,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 127,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7920` | 2,970,000.00 USD | 2,970,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 2,950,000.00 USD | 2,950,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 2,920,000.00 USD | 2,920,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 2,900,000.00 USD | 2,900,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 2,870,000.00 USD | 2,870,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 2,850,000.00 USD | 2,850,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 2,830,000.00 USD | 2,830,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 2,820,000.00 USD | 2,820,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 2,780,000.00 USD | 2,780,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 2,770,000.00 USD | 2,770,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 2,760,000.00 USD | 2,760,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 127,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 2,730,000.00 USD | 2,730,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 2,670,000.00 USD | 2,670,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 2,620,000.00 USD | 2,620,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 2,590,000.00 USD | 2,590,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 126,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 2,580,000.00 USD | 2,580,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 124,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 2,420,000.00 USD | 2,420,000.00 USD | 15,220.00 USD | 3,960.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8240` | 2,550,000.00 USD | 2,550,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8260` | 2,390,000.00 USD | 2,390,000.00 USD | 3,220.00 USD | 8,710.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 2,520,000.00 USD | 2,520,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8280` | 2,380,000.00 USD | 2,380,000.00 USD | 244.70 USD | 1,600.00 USD | 110.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 2,380,000.00 USD | 2,380,000.00 USD | 295.97 USD | 1,440.00 USD | 3,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 2,500,000.00 USD | 2,500,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 2,370,000.00 USD | 2,370,000.00 USD | 2,130.00 USD | 1,910.00 USD | 3,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 2,360,000.00 USD | 2,360,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 2,480,000.00 USD | 2,480,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 2,320,000.00 USD | 2,320,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 124,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8380` | 2,310,000.00 USD | 2,310,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 2,430,000.00 USD | 2,430,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 2,290,000.00 USD | 2,290,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 123,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 2,280,000.00 USD | 2,280,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8420` | 2,410,000.00 USD | 2,410,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 751.39 USD | 122,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 2,280,000.00 USD | 2,280,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8440` | 2,390,000.00 USD | 2,390,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8460` | 2,280,000.00 USD | 2,280,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 2,390,000.00 USD | 2,390,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8480` | 2,250,000.00 USD | 2,250,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 2,380,000.00 USD | 2,380,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 121,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 2,250,000.00 USD | 2,250,000.00 USD | 6,130.00 USD | 371.56 USD | 744.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8500` | 2,340,000.00 USD | 2,340,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 120,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 2,240,000.00 USD | 2,240,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8520` | 2,340,000.00 USD | 2,340,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 2,220,000.00 USD | 2,220,000.00 USD | 2,120.00 USD | 4,890.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 2,330,000.00 USD | 2,330,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 2,210,000.00 USD | 2,210,000.00 USD | 16,070.00 USD | 306.64 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 117,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 2,200,000.00 USD | 2,200,000.00 USD | 2,410.00 USD | 209.22 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8580` | 2,320,000.00 USD | 2,320,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 180.75 USD | 116,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 2,190,000.00 USD | 2,190,000.00 USD | 6,860.00 USD | 10,590.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8600` | 2,310,000.00 USD | 2,310,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 2,160,000.00 USD | 2,160,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,310,000.00 USD | 2,310,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 116,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 2,130,000.00 USD | 2,130,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,270,000.00 USD | 2,270,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8660` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,260,000.00 USD | 2,260,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8680` | 2,080,000.00 USD | 2,080,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 2,190,000.00 USD | 2,190,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 2,010,000.00 USD | 2,010,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8700` | 2,040,000.00 USD | 2,040,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 92,580.00 USD | 102,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,930,000.00 USD | 1,930,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8720` | 1,940,000.00 USD | 1,940,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,840,000.00 USD | 1,840,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,730,000.00 USD | 1,730,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 1,890,000.00 USD | 1,890,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 1,880,000.00 USD | 1,880,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,650,000.00 USD | 1,650,000.00 USD | 10,360.00 USD | 0.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 1,790,000.00 USD | 1,790,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,620,000.00 USD | 1,620,000.00 USD | 1,570.00 USD | 17,400.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 1,780,000.00 USD | 1,780,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,600,000.00 USD | 1,600,000.00 USD | 66,160.00 USD | 28,300.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 1,750,000.00 USD | 1,750,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 1,500,000.00 USD | 1,500,000.00 USD | 73,520.00 USD | 14,120.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 1,510,000.00 USD | 1,510,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 1,380,000.00 USD | 1,380,000.00 USD | 375.79 USD | 51,720.00 USD | 910.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 1,340,000.00 USD | 1,340,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 1,320,000.00 USD | 1,320,000.00 USD | 45,120.00 USD | 32,720.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 1,160,000.00 USD | 1,160,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 1,190,000.00 USD | 1,190,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 1,060,000.00 USD | 1,060,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 1,150,000.00 USD | 1,150,000.00 USD | 2,010.00 USD | 26,350.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 974,610.00 USD | 974,610.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 849,060.00 USD | 849,060.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 831,190.00 USD | 831,190.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 9,960.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 808,590.00 USD | 808,590.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 1,060,000.00 USD | 1,060,000.00 USD | 6,880.00 USD | 21,080.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 740,950.00 USD | 740,950.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 1,010,000.00 USD | 1,010,000.00 USD | 10,660.00 USD | 0.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 992,120.00 USD | 992,120.00 USD | 6,530.00 USD | 6,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 979,030.00 USD | 979,030.00 USD | 0.00 USD | 0.00 USD | 333.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 978,700.00 USD | 978,700.00 USD | 27,150.00 USD | 2,020.00 USD | 231.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 949,290.00 USD | 949,290.00 USD | 4,020.00 USD | 3,740.00 USD | 7,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 728,660.00 USD | 728,660.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 934,520.00 USD | 934,520.00 USD | 0.00 USD | 5,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9200` | 928,600.00 USD | 928,600.00 USD | 5,710.00 USD | 0.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 707,430.00 USD | 707,430.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9220` | 919,170.00 USD | 919,170.00 USD | 0.00 USD | 0.00 USD | 48.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 703,460.00 USD | 703,460.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9240` | 919,130.00 USD | 919,130.00 USD | 66,410.00 USD | 8,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 550,980.00 USD | 550,980.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9260` | 844,090.00 USD | 844,090.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 363,130.00 USD | 363,130.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9280` | 772,360.00 USD | 772,360.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 330,830.00 USD | 330,830.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9300` | 623,640.00 USD | 623,640.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9320` | 614,190.00 USD | 614,190.00 USD | 0.00 USD | 68.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 304,680.00 USD | 304,680.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9340` | 614,120.00 USD | 614,120.00 USD | 93,080.00 USD | 15,100.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 267,230.00 USD | 267,230.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9360` | 504,800.00 USD | 504,800.00 USD | 90,760.00 USD | 45,320.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 255,310.00 USD | 255,310.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9380` | 352,360.00 USD | 352,360.00 USD | 54,410.00 USD | 13,050.00 USD | 1,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 245,290.00 USD | 245,290.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9400` | 283,700.00 USD | 283,700.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9400` | 155,410.00 USD | 155,410.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9420` | 158,330.00 USD | 158,330.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 125,520.00 USD | 125,520.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 251,040.00 USD | 251,040.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 206,470.00 USD | 206,470.00 USD | 140,870.00 USD | 34,100.00 USD | 31,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 459,900.00 USD | 459,900.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 420,590.00 USD | 420,590.00 USD | 97,320.00 USD | 54,970.00 USD | 61,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 840,840.00 USD | 840,840.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 616,170.00 USD | 616,170.00 USD | 110,860.00 USD | 10,350.00 USD | 74,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 1,140,000.00 USD | 1,140,000.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 743,170.00 USD | 743,170.00 USD | 108,100.00 USD | 17,420.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 1,520,000.00 USD | 1,520,000.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 848,590.00 USD | 848,590.00 USD | 31,610.00 USD | 18,130.00 USD | 55,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 1,850,000.00 USD | 1,850,000.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 926,880.00 USD | 926,880.00 USD | 49,650.00 USD | 10,390.00 USD | 18,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 957,900.00 USD | 957,900.00 USD | 10,720.00 USD | 20,030.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 984,250.00 USD | 984,250.00 USD | 4,400.00 USD | 9,570.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 2,010,000.00 USD | 2,010,000.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 998,310.00 USD | 998,310.00 USD | 3,440.00 USD | 8,890.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 2,040,000.00 USD | 2,040,000.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 1,080,000.00 USD | 1,080,000.00 USD | 59,980.00 USD | 7,410.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 2,070,000.00 USD | 2,070,000.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 1,160,000.00 USD | 1,160,000.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 2,190,000.00 USD | 2,190,000.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,210,000.00 USD | 1,210,000.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 2,200,000.00 USD | 2,200,000.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 1,260,000.00 USD | 1,260,000.00 USD | 39,090.00 USD | 12,230.00 USD | 115.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 2,240,000.00 USD | 2,240,000.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9695` | 14,720.00 USD | 14,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,290,000.00 USD | 1,290,000.00 USD | 9,060.00 USD | 4,190.00 USD | 22,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9700` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,340,000.00 USD | 1,340,000.00 USD | 24,360.00 USD | 395.16 USD | 27,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 2,310,000.00 USD | 2,310,000.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,390,000.00 USD | 1,390,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 2,350,000.00 USD | 2,350,000.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 214.00 USD | 14,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,470,000.00 USD | 1,470,000.00 USD | 53,500.00 USD | 20,490.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 2,420,000.00 USD | 2,420,000.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,530,000.00 USD | 1,530,000.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,600,000.00 USD | 1,600,000.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,630,000.00 USD | 1,630,000.00 USD | 16,350.00 USD | 11,710.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 2,770,000.00 USD | 2,770,000.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 1,680,000.00 USD | 1,680,000.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 2,850,000.00 USD | 2,850,000.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 1,760,000.00 USD | 1,760,000.00 USD | 50,550.00 USD | 3,630.00 USD | 24,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 1,790,000.00 USD | 1,790,000.00 USD | 17,200.00 USD | 151.21 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 2,960,000.00 USD | 2,960,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 1,870,000.00 USD | 1,870,000.00 USD | 57,390.00 USD | 1,300.00 USD | 11,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 2,980,000.00 USD | 2,980,000.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 1,900,000.00 USD | 1,900,000.00 USD | 9,580.00 USD | 4,160.00 USD | 21,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 3,000,000.00 USD | 3,000,000.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 1,940,000.00 USD | 1,940,000.00 USD | 25,660.00 USD | 10,700.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 3,050,000.00 USD | 3,050,000.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 1,970,000.00 USD | 1,970,000.00 USD | 18,530.00 USD | 1,480.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 3,170,000.00 USD | 3,170,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 2,050,000.00 USD | 2,050,000.00 USD | 53,500.00 USD | 10,730.00 USD | 15,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 3,230,000.00 USD | 3,230,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,140,000.00 USD | 2,140,000.00 USD | 60,090.00 USD | 23,090.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,290,000.00 USD | 3,290,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,160,000.00 USD | 2,160,000.00 USD | 13,430.00 USD | 1,930.00 USD | 7,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,380,000.00 USD | 3,380,000.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,190,000.00 USD | 2,190,000.00 USD | 10,110.00 USD | 9,550.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,460,000.00 USD | 3,460,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,330,000.00 USD | 2,330,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,520,000.00 USD | 3,520,000.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 15,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,390,000.00 USD | 2,390,000.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,420,000.00 USD | 2,420,000.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,580,000.00 USD | 3,580,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,460,000.00 USD | 2,460,000.00 USD | 16,480.00 USD | 22,350.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,650,000.00 USD | 3,650,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,500,000.00 USD | 2,500,000.00 USD | 6,250.00 USD | 5,790.00 USD | 21,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,680,000.00 USD | 3,680,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,550,000.00 USD | 2,550,000.00 USD | 14,730.00 USD | 25,460.00 USD | 11,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,720,000.00 USD | 3,720,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,600,000.00 USD | 2,600,000.00 USD | 23,750.00 USD | 4,210.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,670,000.00 USD | 2,670,000.00 USD | 46,900.00 USD | 9,980.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,930,000.00 USD | 3,930,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,760,000.00 USD | 2,760,000.00 USD | 40,340.00 USD | 21,340.00 USD | 29,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,150,000.00 USD | 4,150,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,860,000.00 USD | 2,860,000.00 USD | 51,740.00 USD | 12,350.00 USD | 34,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,370,000.00 USD | 4,370,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 40,090.00 USD | 18,290.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,550,000.00 USD | 4,550,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 2,990,000.00 USD | 2,990,000.00 USD | 19,210.00 USD | 8,920.00 USD | 15,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,880,000.00 USD | 4,880,000.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,080,000.00 USD | 3,080,000.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,070,000.00 USD | 5,070,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,150,000.00 USD | 3,150,000.00 USD | 30,760.00 USD | 7,090.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,170,000.00 USD | 5,170,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,190,000.00 USD | 3,190,000.00 USD | 12,440.00 USD | 8,670.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,400,000.00 USD | 5,400,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,200,000.00 USD | 3,200,000.00 USD | 4,520.00 USD | 10,280.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,710,000.00 USD | 5,710,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,250,000.00 USD | 3,250,000.00 USD | 40,430.00 USD | 767.34 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,090,000.00 USD | 6,090,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 15,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,270,000.00 USD | 3,270,000.00 USD | 5,910.00 USD | 6,130.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 10,240.00 USD | 5,750.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,800,000.00 USD | 6,800,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 2,350.00 USD | 1,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 7,060,000.00 USD | 7,060,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,470,000.00 USD | 7,470,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 15,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,860,000.00 USD | 7,860,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,030,000.00 USD | 8,030,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,350,000.00 USD | 8,350,000.00 USD | 141,110.00 USD | 49,780.00 USD | 134,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,520,000.00 USD | 8,520,000.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,880,000.00 USD | 8,880,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,240,000.00 USD | 9,240,000.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,660,000.00 USD | 9,660,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,940,000.00 USD | 9,940,000.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 10,180,000.00 USD | 10,180,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,370,000.00 USD | 10,370,000.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,710,000.00 USD | 10,710,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,910,000.00 USD | 10,910,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,130,000.00 USD | 11,130,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,330,000.00 USD | 11,330,000.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,480,000.00 USD | 11,480,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,750,000.00 USD | 11,750,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,990,000.00 USD | 11,990,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 17,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,110,000.00 USD | 12,110,000.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,290,000.00 USD | 12,290,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,520,000.00 USD | 12,520,000.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,760,000.00 USD | 12,760,000.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,920,000.00 USD | 12,920,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,040,000.00 USD | 13,040,000.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,200,000.00 USD | 13,200,000.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,360,000.00 USD | 13,360,000.00 USD | 66,380.00 USD | 32,080.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,600,000.00 USD | 13,600,000.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,890,000.00 USD | 13,890,000.00 USD | 182,190.00 USD | 62,380.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,960,000.00 USD | 13,960,000.00 USD | 59,740.00 USD | 10,900.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 18,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 20,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 42,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 54,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 54,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 57,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 120.08 USD | 58,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 58,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 60,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 801.29 USD | 60,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 63,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 71,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 71,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 246.88 USD | 72,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 123.39 USD | 72,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 330.93 USD | 72,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 72,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 90,490.00 USD | 163,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 23,940.00 USD | 187,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 208.37 USD | 187,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2135` | 441,430.00 USD | 0.00 USD | 366.26 USD | `-77.04%` | `1,715.50` |
| `Live` | `Long` | `0.2275` | 441,070.00 USD | 0.00 USD | 113.75 USD | `-75.53%` | `500.00` |
| `Live` | `Long` | `0.3615` | 440,950.00 USD | 0.00 USD | 798.55 USD | `-61.12%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 440,150.00 USD | 0.00 USD | 2,800.00 USD | `-54.89%` | `6,675.20` |
| `Live` | `Long` | `0.4275` | 437,350.00 USD | 0.00 USD | 2,440.00 USD | `-54.03%` | `5,698.80` |
| `Live` | `Long` | `0.4645` | 434,920.00 USD | 0.00 USD | 315.16 USD | `-50.05%` | `678.50` |
| `Live` | `Long` | `0.4675` | 434,600.00 USD | 0.00 USD | 146.70 USD | `-49.73%` | `313.80` |
| `Live` | `Long` | `0.4705` | 434,450.00 USD | 0.00 USD | 2,590.00 USD | `-49.40%` | `5,500.00` |
| `Live` | `Long` | `0.4915` | 431,870.00 USD | 0.00 USD | 1,290.00 USD | `-47.14%` | `2,618.10` |
| `Live` | `Long` | `0.5065` | 430,580.00 USD | 0.00 USD | 3,290.00 USD | `-45.53%` | `6,504.70` |
| `Live` | `Long` | `0.5405` | 427,290.00 USD | 0.00 USD | 540.50 USD | `-41.87%` | `1,000.00` |
| `Live` | `Long` | `0.5645` | 426,740.00 USD | 0.00 USD | 223.82 USD | `-39.29%` | `396.50` |
| `Live` | `Long` | `0.5655` | 426,520.00 USD | 0.00 USD | 14,600.00 USD | `-39.19%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 411,920.00 USD | 0.00 USD | 577.36 USD | `-38.76%` | `1,013.80` |
| `Live` | `Long` | `0.5785` | 411,340.00 USD | 0.00 USD | 151.62 USD | `-37.79%` | `262.10` |
| `Live` | `Long` | `0.5845` | 411,190.00 USD | 0.00 USD | 683.51 USD | `-37.14%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 410,510.00 USD | 0.00 USD | 137.53 USD | `-36.61%` | `233.30` |
| `Live` | `Long` | `0.6055` | 410,370.00 USD | 0.00 USD | 1,480.00 USD | `-34.88%` | `2,448.50` |
| `Live` | `Long` | `0.6065` | 408,890.00 USD | 0.00 USD | 1,800.00 USD | `-34.78%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 407,090.00 USD | 0.00 USD | 105.96 USD | `-34.13%` | `173.00` |
| `Live` | `Long` | `0.6145` | 406,980.00 USD | 0.00 USD | 147.48 USD | `-33.92%` | `240.00` |
| `Live` | `Long` | `0.6165` | 406,830.00 USD | 0.00 USD | 247.03 USD | `-33.70%` | `400.70` |
| `Live` | `Long` | `0.6315` | 406,590.00 USD | 0.00 USD | 757.80 USD | `-32.09%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 405,830.00 USD | 0.00 USD | 106.00 USD | `-31.66%` | `166.80` |
| `Live` | `Long` | `0.6365` | 405,720.00 USD | 0.00 USD | 507.86 USD | `-31.55%` | `797.90` |
| `Live` | `Long` | `0.6405` | 405,210.00 USD | 0.00 USD | 2,090.00 USD | `-31.12%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 403,130.00 USD | 0.00 USD | 20,270.00 USD | `-31.01%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 382,860.00 USD | 0.00 USD | 4,230.00 USD | `-30.48%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 378,630.00 USD | 0.00 USD | 202.47 USD | `-30.37%` | `312.70` |
| `Live` | `Long` | `0.6595` | 378,430.00 USD | 0.00 USD | 149.44 USD | `-29.08%` | `226.60` |
| `Live` | `Long` | `0.6725` | 378,280.00 USD | 0.00 USD | 63,890.00 USD | `-27.68%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 314,390.00 USD | 0.00 USD | 423.10 USD | `-27.14%` | `624.50` |
| `Live` | `Long` | `0.6805` | 313,970.00 USD | 0.00 USD | 85,060.00 USD | `-26.82%` | `125,000.00` |
| `Live` | `Long` | `0.6835` | 228,900.00 USD | 0.00 USD | 512.97 USD | `-26.50%` | `750.50` |
| `Live` | `Long` | `0.6965` | 228,390.00 USD | 0.00 USD | 478.22 USD | `-25.10%` | `686.60` |
| `Live` | `Long` | `0.6985` | 227,910.00 USD | 0.00 USD | 20,000.00 USD | `-24.88%` | `28,635.00` |
| `Live` | `Long` | `0.7005` | 207,910.00 USD | 0.00 USD | 1,140.00 USD | `-24.67%` | `1,634.20` |
| `Live` | `Long` | `0.7145` | 206,770.00 USD | 0.00 USD | 988.87 USD | `-23.16%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 205,780.00 USD | 0.00 USD | 1,580.00 USD | `-22.41%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 204,200.00 USD | 0.00 USD | 397.93 USD | `-22.20%` | `550.00` |
| `Live` | `Long` | `0.7285` | 203,800.00 USD | 0.00 USD | 291.18 USD | `-21.66%` | `399.70` |
| `Live` | `Long` | `0.7305` | 203,510.00 USD | 0.00 USD | 2,300.00 USD | `-21.44%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 201,210.00 USD | 0.00 USD | 1,140.00 USD | `-21.12%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 200,070.00 USD | 0.00 USD | 283.30 USD | `-20.47%` | `383.10` |
| `Live` | `Long` | `0.7525` | 199,790.00 USD | 0.00 USD | 331.18 USD | `-19.08%` | `440.10` |
| `Live` | `Long` | `0.7535` | 199,450.00 USD | 0.00 USD | 1,400.00 USD | `-18.97%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 198,050.00 USD | 0.00 USD | 8,990.00 USD | `-18.75%` | `11,902.80` |
| `Live` | `Long` | `0.7615` | 189,060.00 USD | 0.00 USD | 54,070.00 USD | `-18.11%` | `71,003.30` |
| `Live` | `Long` | `0.7635` | 134,990.00 USD | 0.00 USD | 308.00 USD | `-17.89%` | `403.40` |
| `Live` | `Long` | `0.7725` | 134,680.00 USD | 0.00 USD | 3,840.00 USD | `-16.93%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 130,850.00 USD | 0.00 USD | 2,490.00 USD | `-16.39%` | `3,199.30` |
| `Live` | `Long` | `0.7795` | 128,360.00 USD | 0.00 USD | 272.83 USD | `-16.17%` | `350.00` |
| `Live` | `Long` | `0.7865` | 128,080.00 USD | 0.00 USD | 292.03 USD | `-15.42%` | `371.30` |
| `Live` | `Long` | `0.7905` | 127,790.00 USD | 0.00 USD | 277.39 USD | `-14.99%` | `350.90` |
| `Live` | `Long` | `0.8135` | 127,520.00 USD | 0.00 USD | 647.79 USD | `-12.52%` | `796.30` |
| `Live` | `Long` | `0.8215` | 126,870.00 USD | 0.00 USD | 1,950.00 USD | `-11.66%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 124,920.00 USD | 0.00 USD | 749.96 USD | `-11.44%` | `910.70` |
| `Live` | `Long` | `0.8365` | 124,170.00 USD | 0.00 USD | 316.70 USD | `-10.04%` | `378.60` |
| `Live` | `Long` | `0.8415` | 123,850.00 USD | 0.00 USD | 1,570.00 USD | `-9.51%` | `1,862.40` |
| `Live` | `Long` | `0.8435` | 122,290.00 USD | 0.00 USD | 751.39 USD | `-9.29%` | `890.80` |
| `Live` | `Long` | `0.8495` | 121,530.00 USD | 0.00 USD | 1,260.00 USD | `-8.65%` | `1,486.90` |
| `Live` | `Long` | `0.8515` | 120,270.00 USD | 0.00 USD | 2,700.00 USD | `-8.43%` | `3,175.90` |
| `Live` | `Long` | `0.8575` | 117,570.00 USD | 0.00 USD | 620.32 USD | `-7.78%` | `723.40` |
| `Live` | `Long` | `0.8595` | 116,950.00 USD | 0.00 USD | 180.75 USD | `-7.57%` | `210.30` |
| `Live` | `Long` | `0.8635` | 116,770.00 USD | 0.00 USD | 208.02 USD | `-7.14%` | `240.90` |
| `Live` | `Long` | `0.8645` | 116,560.00 USD | 0.00 USD | 438.30 USD | `-7.03%` | `507.00` |
| `Live` | `Long` | `0.8665` | 116,120.00 USD | 0.00 USD | 1,390.00 USD | `-6.82%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 114,730.00 USD | 0.00 USD | 12,590.00 USD | `-6.49%` | `14,478.80` |
| `Live` | `Long` | `0.8715` | 102,140.00 USD | 0.00 USD | 92,580.00 USD | `-6.28%` | `106,233.40` |
| `Live` | `Long` | `0.8765` | 9,560.00 USD | 0.00 USD | 9,560.00 USD | `-5.74%` | `10,903.10` |
| `Live` | `Short` | `0.9695` | 14,720.00 USD | 14,720.00 USD | 0.00 USD | `+4.26%` | `15,182.70` |
| `Live` | `Short` | `0.9745` | 14,930.00 USD | 214.00 USD | 0.00 USD | `+4.80%` | `219.60` |
| `Live` | `Short` | `1.01` | 15,150.00 USD | 221.13 USD | 0.00 USD | `+8.24%` | `219.70` |
| `Live` | `Short` | `1.04` | 15,380.00 USD | 228.37 USD | 0.00 USD | `+11.68%` | `219.90` |
| `Live` | `Short` | `1.05` | 15,750.00 USD | 367.04 USD | 0.00 USD | `+12.65%` | `350.40` |
| `Live` | `Short` | `1.08` | 17,980.00 USD | 2,230.00 USD | 0.00 USD | `+16.30%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 18,150.00 USD | 170.02 USD | 0.00 USD | `+19.42%` | `153.10` |
| `Live` | `Short` | `1.17` | 20,610.00 USD | 2,450.00 USD | 0.00 USD | `+25.88%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 42,790.00 USD | 22,180.00 USD | 0.00 USD | `+27.81%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 54,520.00 USD | 11,730.00 USD | 0.00 USD | `+42.33%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 54,760.00 USD | 239.77 USD | 0.00 USD | `+44.05%` | `179.00` |
| `Live` | `Short` | `1.42` | 57,950.00 USD | 3,190.00 USD | 0.00 USD | `+52.65%` | `2,249.30` |
| `Live` | `Short` | `1.51` | 58,070.00 USD | 120.08 USD | 0.00 USD | `+62.44%` | `79.50` |
| `Live` | `Short` | `1.54` | 58,250.00 USD | 176.31 USD | 0.00 USD | `+65.88%` | `114.30` |
| `Live` | `Short` | `1.56` | 60,060.00 USD | 1,810.00 USD | 0.00 USD | `+67.39%` | `1,161.90` |
| `Live` | `Short` | `1.60` | 60,860.00 USD | 801.29 USD | 0.00 USD | `+72.55%` | `499.40` |
| `Live` | `Short` | `1.62` | 63,290.00 USD | 2,440.00 USD | 0.00 USD | `+74.70%` | `1,500.00` |
| `Live` | `Short` | `1.65` | 71,530.00 USD | 8,240.00 USD | 0.00 USD | `+77.17%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 71,830.00 USD | 300.15 USD | 0.00 USD | `+79.32%` | `180.00` |
| `Live` | `Short` | `1.69` | 72,080.00 USD | 246.88 USD | 0.00 USD | `+81.47%` | `146.30` |
| `Live` | `Short` | `1.72` | 72,200.00 USD | 123.39 USD | 0.00 USD | `+84.81%` | `71.80` |
| `Live` | `Short` | `1.72` | 72,530.00 USD | 330.93 USD | 0.00 USD | `+85.45%` | `191.90` |
| `Live` | `Short` | `1.73` | 72,720.00 USD | 190.42 USD | 0.00 USD | `+85.99%` | `110.10` |
| `Live` | `Short` | `1.82` | 163,210.00 USD | 90,490.00 USD | 0.00 USD | `+95.56%` | `49,759.80` |
| `Live` | `Short` | `1.85` | 187,150.00 USD | 23,940.00 USD | 0.00 USD | `+99.32%` | `12,916.90` |
| `Live` | `Short` | `1.86` | 187,360.00 USD | 208.37 USD | 0.00 USD | `+99.54%` | `112.30` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 347,140.00 USD | 0.00 USD | 120.45 USD | `-56.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 347,020.00 USD | 0.00 USD | 150.15 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 346,870.00 USD | 0.00 USD | 186.15 USD | `-41.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 346,690.00 USD | 0.00 USD | 1,150.00 USD | `-29.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 345,540.00 USD | 0.00 USD | 781.90 USD | `-24.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 344,760.00 USD | 0.00 USD | 477.38 USD | `-23.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 344,280.00 USD | 0.00 USD | 341.33 USD | `-22.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 343,940.00 USD | 0.00 USD | 972.82 USD | `-22.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 342,960.00 USD | 0.00 USD | 160.20 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 342,800.00 USD | 0.00 USD | 102.58 USD | `-20.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 342,700.00 USD | 0.00 USD | 289.49 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 342,410.00 USD | 0.00 USD | 197.53 USD | `-18.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 342,210.00 USD | 0.00 USD | 14,570.00 USD | `-16.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 327,650.00 USD | 0.00 USD | 213.58 USD | `-15.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 327,430.00 USD | 0.00 USD | 274,830.00 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 52,600.00 USD | 0.00 USD | 108.47 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 52,490.00 USD | 0.00 USD | 326.96 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 52,160.00 USD | 0.00 USD | 405.75 USD | `-12.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 51,760.00 USD | 0.00 USD | 772.84 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 50,990.00 USD | 0.00 USD | 2,670.00 USD | `-9.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 48,310.00 USD | 0.00 USD | 3,470.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 44,840.00 USD | 0.00 USD | 9,180.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 35,660.00 USD | 0.00 USD | 341.94 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 35,320.00 USD | 0.00 USD | 1,150.00 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 34,170.00 USD | 0.00 USD | 429.25 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 33,750.00 USD | 0.00 USD | 223.30 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 33,520.00 USD | 0.00 USD | 518.51 USD | `-6.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 33,000.00 USD | 0.00 USD | 205.24 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 32,800.00 USD | 0.00 USD | 649.66 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 32,150.00 USD | 0.00 USD | 194.06 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 31,950.00 USD | 0.00 USD | 193.35 USD | `-4.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 31,760.00 USD | 0.00 USD | 223.04 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 31,540.00 USD | 0.00 USD | 10,840.00 USD | `-4.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 20,690.00 USD | 0.00 USD | 4,920.00 USD | `-4.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 15,780.00 USD | 0.00 USD | 317.02 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 15,460.00 USD | 0.00 USD | 192.07 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 15,270.00 USD | 0.00 USD | 195.32 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 15,070.00 USD | 0.00 USD | 196.87 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 14,880.00 USD | 0.00 USD | 2,870.00 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 12,000.00 USD | 0.00 USD | 319.05 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 11,680.00 USD | 0.00 USD | 398.91 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 11,280.00 USD | 0.00 USD | 196.96 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 11,090.00 USD | 0.00 USD | 300.38 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 10,790.00 USD | 0.00 USD | 198.61 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 10,590.00 USD | 0.00 USD | 994.35 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 9,590.00 USD | 0.00 USD | 363.40 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 9,230.00 USD | 0.00 USD | 198.18 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 9,030.00 USD | 0.00 USD | 397.23 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 8,630.00 USD | 0.00 USD | 398.65 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 8,240.00 USD | 0.00 USD | 399.09 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 7,840.00 USD | 0.00 USD | 403.92 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 7,430.00 USD | 0.00 USD | 198.06 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 7,230.00 USD | 0.00 USD | 223.78 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9185` | 7,010.00 USD | 0.00 USD | 899.85 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9195` | 6,110.00 USD | 0.00 USD | 900.19 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9205` | 5,210.00 USD | 0.00 USD | 407.41 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9215` | 4,800.00 USD | 0.00 USD | 407.30 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9225` | 4,400.00 USD | 0.00 USD | 201.94 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9245` | 4,190.00 USD | 0.00 USD | 201.45 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9255` | 3,990.00 USD | 0.00 USD | 817.40 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9265` | 3,180.00 USD | 0.00 USD | 403.77 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9275` | 2,770.00 USD | 0.00 USD | 2,120.00 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9285` | 653.55 USD | 0.00 USD | 246.05 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9295` | 407.49 USD | 0.00 USD | 407.49 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 203.97 USD | 203.97 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 467.77 USD | 263.80 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 709.75 USD | 241.98 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 1,520.00 USD | 814.76 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 1,730.00 USD | 201.97 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 11,410.00 USD | 9,680.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 11,830.00 USD | 416.01 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 12,380.00 USD | 555.18 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 13,200.00 USD | 816.96 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9435` | 13,530.00 USD | 334.28 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 15,260.00 USD | 1,730.00 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 15,640.00 USD | 383.87 USD | 0.00 USD | `+1.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 16,270.00 USD | 623.93 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 16,680.00 USD | 414.68 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 17,060.00 USD | 381.00 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 19,080.00 USD | 2,020.00 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 19,290.00 USD | 206.77 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 19,520.00 USD | 236.26 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 19,660.00 USD | 136.83 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 19,920.00 USD | 261.16 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 21,830.00 USD | 1,910.00 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 22,400.00 USD | 568.75 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 22,560.00 USD | 163.29 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 22,950.00 USD | 385.74 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 24,980.00 USD | 2,030.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 25,240.00 USD | 262.52 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 25,630.00 USD | 387.83 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 33,260.00 USD | 7,630.00 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 42,010.00 USD | 8,750.00 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 63,970.00 USD | 21,960.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 64,370.00 USD | 396.17 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 65,040.00 USD | 676.53 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 73,400.00 USD | 8,350.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 75,420.00 USD | 2,030.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 77,480.00 USD | 2,060.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 77,740.00 USD | 255.38 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 92,810.00 USD | 15,070.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 92,920.00 USD | 109.99 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 127,890.00 USD | 34,970.00 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 131,410.00 USD | 3,520.00 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 163,170.00 USD | 31,750.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 163,570.00 USD | 403.06 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 163,970.00 USD | 403.28 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 169,120.00 USD | 5,140.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 206,420.00 USD | 37,310.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 207,420.00 USD | 1,000.00 USD | 0.00 USD | `+7.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 248,020.00 USD | 40,590.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 248,260.00 USD | 235.79 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 249,600.00 USD | 1,340.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 249,830.00 USD | 230.39 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 250,050.00 USD | 218.64 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 250,460.00 USD | 409.86 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 250,570.00 USD | 110.95 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 251,180.00 USD | 615.60 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 251,750.00 USD | 561.17 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 251,960.00 USD | 214.40 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 252,210.00 USD | 249.88 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 252,420.00 USD | 207.97 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 252,630.00 USD | 208.26 USD | 0.00 USD | `+10.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 253,140.00 USD | 516.75 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 253,490.00 USD | 348.86 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 253,880.00 USD | 391.80 USD | 0.00 USD | `+11.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 254,300.00 USD | 413.76 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 254,650.00 USD | 354.91 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 256,560.00 USD | 1,900.00 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 256,760.00 USD | 207.87 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 256,970.00 USD | 207.97 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 257,080.00 USD | 107.99 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 331,920.00 USD | 74,840.00 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 332,460.00 USD | 544.88 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 334,630.00 USD | 2,170.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 336,170.00 USD | 1,540.00 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 346,090.00 USD | 9,930.00 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 346,970.00 USD | 877.63 USD | 0.00 USD | `+19.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 347,140.00 USD | 171.09 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 349,910.00 USD | 2,770.00 USD | 0.00 USD | `+20.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 351,950.00 USD | 2,040.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 352,120.00 USD | 172.32 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 352,310.00 USD | 187.72 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 352,500.00 USD | 188.39 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 355,170.00 USD | 2,670.00 USD | 0.00 USD | `+22.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 355,340.00 USD | 174.23 USD | 0.00 USD | `+22.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 355,510.00 USD | 174.38 USD | 0.00 USD | `+22.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 355,690.00 USD | 174.84 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 355,840.00 USD | 150.90 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 355,990.00 USD | 151.03 USD | 0.00 USD | `+23.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 356,140.00 USD | 151.16 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 356,290.00 USD | 151.29 USD | 0.00 USD | `+23.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 358,340.00 USD | 2,050.00 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 358,450.00 USD | 110.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 358,930.00 USD | 475.80 USD | 0.00 USD | `+27.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 360,140.00 USD | 1,210.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 403,060.00 USD | 42,930.00 USD | 0.00 USD | `+29.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 405,070.00 USD | 2,000.00 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 406,450.00 USD | 1,380.00 USD | 0.00 USD | `+34.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 406,700.00 USD | 245.41 USD | 0.00 USD | `+37.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 415,090.00 USD | 8,390.00 USD | 0.00 USD | `+38.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 415,510.00 USD | 415.25 USD | 0.00 USD | `+39.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 422,020.00 USD | 6,520.00 USD | 0.00 USD | `+40.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 426,820.00 USD | 4,800.00 USD | 0.00 USD | `+40.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 427,470.00 USD | 655.75 USD | 0.00 USD | `+41.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 428,070.00 USD | 596.43 USD | 0.00 USD | `+43.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 429,890.00 USD | 1,810.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 443,770.00 USD | 13,880.00 USD | 0.00 USD | `+44.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 445,020.00 USD | 1,250.00 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 447,090.00 USD | 2,070.00 USD | 0.00 USD | `+49.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 447,230.00 USD | 140.05 USD | 0.00 USD | `+50.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 447,390.00 USD | 160.42 USD | 0.00 USD | `+50.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 448,340.00 USD | 954.32 USD | 0.00 USD | `+51.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 482,520.00 USD | 34,170.00 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 483,400.00 USD | 879.84 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 486,450.00 USD | 3,050.00 USD | 0.00 USD | `+62.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 486,750.00 USD | 297.27 USD | 0.00 USD | `+66.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 495,280.00 USD | 8,530.00 USD | 0.00 USD | `+77.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 495,420.00 USD | 143.99 USD | 0.00 USD | `+79.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 495,600.00 USD | 177.05 USD | 0.00 USD | `+90.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 496,030.00 USD | 431.40 USD | 0.00 USD | `+93.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 496,250.00 USD | 220.77 USD | 0.00 USD | `+95.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.7700` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD |
| `7D` | `0.7720` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `0.7740` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `0.7760` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD |
| `7D` | `0.7780` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7800` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD |
| `7D` | `0.7820` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD |
| `7D` | `0.7840` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD |
| `7D` | `0.7860` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD |
| `7D` | `0.7880` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD |
| `7D` | `0.7900` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD |
| `7D` | `0.7920` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD |
| `7D` | `0.7940` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD |
| `7D` | `0.7960` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD |
| `7D` | `0.7980` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD |
| `7D` | `0.8000` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD |
| `7D` | `0.8020` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `1D` | `0.8240` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 15,220.00 USD | 3,960.00 USD | 10,500.00 USD |
| `7D` | `0.8240` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `1D` | `0.8260` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 3,220.00 USD | 8,710.00 USD | 971.85 USD |
| `7D` | `0.8260` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `1D` | `0.8280` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 244.70 USD | 1,600.00 USD | 110.11 USD |
| `7D` | `0.8280` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `1D` | `0.8300` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 295.97 USD | 1,440.00 USD | 3,680.00 USD |
| `7D` | `0.8300` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `1D` | `0.8320` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 2,130.00 USD | 1,910.00 USD | 3,450.00 USD |
| `7D` | `0.8320` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `1D` | `0.8340` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 25,550.00 USD | 5,650.00 USD | 8,980.00 USD |
| `7D` | `0.8340` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `1D` | `0.8360` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,870.00 USD | 636.81 USD | 14,840.00 USD |
| `7D` | `0.8360` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8380` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 16,380.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8380` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8400` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 458.00 USD | 1,050.00 USD | 2,340.00 USD |
| `7D` | `0.8400` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8420` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,340.00 USD | 4,840.00 USD | 0.00 USD |
| `7D` | `0.8420` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 2,210.00 USD | 5.65 USD | 0.00 USD |
| `7D` | `0.8440` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8460` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 15,140.00 USD | 6,600.00 USD | 25.04 USD |
| `7D` | `0.8460` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8480` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 6,670.00 USD | 230.58 USD | 0.00 USD |
| `7D` | `0.8480` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.8500` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 6,130.00 USD | 371.56 USD | 744.62 USD |
| `7D` | `0.8500` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD |
| `1D` | `0.8520` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 1,230.00 USD | 1,940.00 USD | 12,140.00 USD |
| `7D` | `0.8520` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8540` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,120.00 USD | 4,890.00 USD | 4,030.00 USD |
| `7D` | `0.8540` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8560` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 16,070.00 USD | 306.64 USD | 0.00 USD |
| `7D` | `0.8560` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8580` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 2,410.00 USD | 209.22 USD | 2,050.00 USD |
| `7D` | `0.8580` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD |
| `1D` | `0.8600` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 6,860.00 USD | 10,590.00 USD | 13,690.00 USD |
| `7D` | `0.8600` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD |
| `1D` | `0.8620` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 12,920.00 USD | 12,720.00 USD | 0.00 USD |
| `7D` | `0.8620` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8640` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 48,740.00 USD | 2,370.00 USD | 3,790.00 USD |
| `7D` | `0.8640` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8660` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 0.00 USD | 3,080.00 USD | 0.00 USD |
| `7D` | `0.8660` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8680` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 43,000.00 USD | 9,030.00 USD | 11,890.00 USD |
| `7D` | `0.8680` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8700` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 49,290.00 USD | 3,880.00 USD | 33,390.00 USD |
| `7D` | `0.8700` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8720` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 30,840.00 USD | 34,140.00 USD | 24,590.00 USD |
| `7D` | `0.8720` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8740` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 59,860.00 USD | 12,180.00 USD | 33,580.00 USD |
| `7D` | `0.8740` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8760` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 16,700.00 USD | 5,410.00 USD | 1,470.00 USD |
| `7D` | `0.8760` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8780` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 214.09 USD | 54,890.00 USD |
| `7D` | `0.8780` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8800` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 10,360.00 USD | 0.00 USD | 7,750.00 USD |
| `7D` | `0.8800` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD |
| `1D` | `0.8820` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 0.00 USD | 10,010.00 USD | 0.00 USD |
| `7D` | `0.8820` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8840` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,570.00 USD | 17,400.00 USD | 8,890.00 USD |
| `7D` | `0.8840` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8860` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 66,160.00 USD | 28,300.00 USD | 2,350.00 USD |
| `7D` | `0.8860` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8880` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 73,520.00 USD | 14,120.00 USD | 36,640.00 USD |
| `7D` | `0.8880` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8900` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 375.79 USD | 51,720.00 USD | 910.96 USD |
| `7D` | `0.8900` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8920` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 45,120.00 USD | 32,720.00 USD | 56,100.00 USD |
| `7D` | `0.8920` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8940` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 13,790.00 USD | 18,130.00 USD | 1,980.00 USD |
| `7D` | `0.8940` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8960` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 2,010.00 USD | 26,350.00 USD | 5,550.00 USD |
| `7D` | `0.8960` | 974,610.00 USD | 0.00 USD | 974,610.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD |
| `1D` | `0.8980` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 26,620.00 USD | 16,170.00 USD |
| `7D` | `0.8980` | 849,060.00 USD | 0.00 USD | 849,060.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD |
| `1D` | `0.9000` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 10,050.00 USD | 0.00 USD |
| `7D` | `0.9000` | 831,190.00 USD | 0.00 USD | 831,190.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `0.9020` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 0.00 USD | 9,960.00 USD | 1,590.00 USD |
| `7D` | `0.9020` | 808,590.00 USD | 0.00 USD | 808,590.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD |
| `1D` | `0.9040` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 6,880.00 USD | 21,080.00 USD | 17,930.00 USD |
| `7D` | `0.9040` | 740,950.00 USD | 0.00 USD | 740,950.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD |
| `1D` | `0.9060` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 10,660.00 USD | 0.00 USD | 7,720.00 USD |
| `1D` | `0.9080` | 992,120.00 USD | 0.00 USD | 992,120.00 USD | 6,530.00 USD | 6,560.00 USD | 0.00 USD |
| `1D` | `0.9100` | 979,030.00 USD | 0.00 USD | 979,030.00 USD | 0.00 USD | 0.00 USD | 333.64 USD |
| `1D` | `0.9120` | 978,700.00 USD | 0.00 USD | 978,700.00 USD | 27,150.00 USD | 2,020.00 USD | 231.60 USD |
| `1D` | `0.9140` | 949,290.00 USD | 0.00 USD | 949,290.00 USD | 4,020.00 USD | 3,740.00 USD | 7,010.00 USD |
| `7D` | `0.9140` | 728,660.00 USD | 0.00 USD | 728,660.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD |
| `1D` | `0.9160` | 934,520.00 USD | 0.00 USD | 934,520.00 USD | 0.00 USD | 5,930.00 USD | 0.00 USD |
| `1D` | `0.9200` | 928,600.00 USD | 0.00 USD | 928,600.00 USD | 5,710.00 USD | 0.00 USD | 3,710.00 USD |
| `7D` | `0.9200` | 707,430.00 USD | 0.00 USD | 707,430.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.9220` | 919,170.00 USD | 0.00 USD | 919,170.00 USD | 0.00 USD | 0.00 USD | 48.22 USD |
| `7D` | `0.9220` | 703,460.00 USD | 0.00 USD | 703,460.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9240` | 919,130.00 USD | 0.00 USD | 919,130.00 USD | 66,410.00 USD | 8,630.00 USD | 0.00 USD |
| `7D` | `0.9240` | 550,980.00 USD | 0.00 USD | 550,980.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD |
| `1D` | `0.9260` | 844,090.00 USD | 0.00 USD | 844,090.00 USD | 898.50 USD | 39,060.00 USD | 31,770.00 USD |
| `7D` | `0.9260` | 363,130.00 USD | 0.00 USD | 363,130.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD |
| `1D` | `0.9280` | 772,360.00 USD | 0.00 USD | 772,360.00 USD | 78,050.00 USD | 4,120.00 USD | 66,550.00 USD |
| `7D` | `0.9280` | 330,830.00 USD | 0.00 USD | 330,830.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9300` | 623,640.00 USD | 0.00 USD | 623,640.00 USD | 0.00 USD | 9,460.00 USD | 0.00 USD |
| `1D` | `0.9320` | 614,190.00 USD | 0.00 USD | 614,190.00 USD | 0.00 USD | 68.90 USD | 0.00 USD |
| `7D` | `0.9320` | 304,680.00 USD | 0.00 USD | 304,680.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9340` | 614,120.00 USD | 0.00 USD | 614,120.00 USD | 93,080.00 USD | 15,100.00 USD | 1,140.00 USD |
| `7D` | `0.9340` | 267,230.00 USD | 0.00 USD | 267,230.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD |
| `1D` | `0.9360` | 504,800.00 USD | 0.00 USD | 504,800.00 USD | 90,760.00 USD | 45,320.00 USD | 16,350.00 USD |
| `7D` | `0.9360` | 255,310.00 USD | 0.00 USD | 255,310.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9380` | 352,360.00 USD | 0.00 USD | 352,360.00 USD | 54,410.00 USD | 13,050.00 USD | 1,210.00 USD |
| `7D` | `0.9380` | 245,290.00 USD | 0.00 USD | 245,290.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9400` | 283,700.00 USD | 0.00 USD | 283,700.00 USD | 88,450.00 USD | 36,910.00 USD | 0.00 USD |
| `7D` | `0.9400` | 155,410.00 USD | 0.00 USD | 155,410.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD |
| `1D` | `0.9420` | 158,330.00 USD | 0.00 USD | 158,330.00 USD | 101,680.00 USD | 20,480.00 USD | 36,170.00 USD |
| `7D` | `0.9420` | 125,520.00 USD | 125,520.00 USD | 0.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD |
| `7D` | `0.9420` | 251,040.00 USD | 251,040.00 USD | 0.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD |
| `1D` | `0.9430` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9440` | 206,470.00 USD | 206,470.00 USD | 0.00 USD | 140,870.00 USD | 34,100.00 USD | 31,500.00 USD |
| `7D` | `0.9440` | 459,900.00 USD | 459,900.00 USD | 0.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD |
| `1D` | `0.9460` | 420,590.00 USD | 420,590.00 USD | 0.00 USD | 97,320.00 USD | 54,970.00 USD | 61,820.00 USD |
| `7D` | `0.9460` | 840,840.00 USD | 840,840.00 USD | 0.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD |
| `1D` | `0.9480` | 616,170.00 USD | 616,170.00 USD | 0.00 USD | 110,860.00 USD | 10,350.00 USD | 74,370.00 USD |
| `7D` | `0.9480` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD |
| `1D` | `0.9500` | 743,170.00 USD | 743,170.00 USD | 0.00 USD | 108,100.00 USD | 17,420.00 USD | 1,480.00 USD |
| `7D` | `0.9500` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD |
| `1D` | `0.9520` | 848,590.00 USD | 848,590.00 USD | 0.00 USD | 31,610.00 USD | 18,130.00 USD | 55,680.00 USD |
| `7D` | `0.9520` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD |
| `1D` | `0.9540` | 926,880.00 USD | 926,880.00 USD | 0.00 USD | 49,650.00 USD | 10,390.00 USD | 18,250.00 USD |
| `7D` | `0.9540` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD |
| `1D` | `0.9560` | 957,900.00 USD | 957,900.00 USD | 0.00 USD | 10,720.00 USD | 20,030.00 USD | 275.27 USD |
| `7D` | `0.9560` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9580` | 984,250.00 USD | 984,250.00 USD | 0.00 USD | 4,400.00 USD | 9,570.00 USD | 12,380.00 USD |
| `7D` | `0.9580` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD |
| `1D` | `0.9600` | 998,310.00 USD | 998,310.00 USD | 0.00 USD | 3,440.00 USD | 8,890.00 USD | 1,720.00 USD |
| `7D` | `0.9600` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9620` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 59,980.00 USD | 7,410.00 USD | 16,600.00 USD |
| `7D` | `0.9620` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD |
| `1D` | `0.9640` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 19,400.00 USD | 30,520.00 USD | 28,000.00 USD |
| `7D` | `0.9640` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD |
| `1D` | `0.9660` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 2,700.00 USD | 4,970.00 USD | 37,190.00 USD |
| `7D` | `0.9660` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9680` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 39,090.00 USD | 12,230.00 USD | 115.80 USD |
| `7D` | `0.9680` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9700` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 9,060.00 USD | 4,190.00 USD | 22,700.00 USD |
| `7D` | `0.9700` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD |
| `1D` | `0.9720` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 24,360.00 USD | 395.16 USD | 27,260.00 USD |
| `7D` | `0.9720` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD |
| `1D` | `0.9740` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD |
| `7D` | `0.9740` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD |
| `1D` | `0.9760` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 53,500.00 USD | 20,490.00 USD | 6,610.00 USD |
| `7D` | `0.9760` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD |
| `1D` | `0.9780` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 40,740.00 USD | 3,080.00 USD | 16,650.00 USD |
| `7D` | `0.9780` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9800` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 34,990.00 USD | 9,680.00 USD | 20,300.00 USD |
| `7D` | `0.9800` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD |
| `1D` | `0.9820` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 16,350.00 USD | 11,710.00 USD | 7,280.00 USD |
| `7D` | `0.9820` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD |
| `1D` | `0.9840` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 665.59 USD | 13,380.00 USD | 38,710.00 USD |
| `7D` | `0.9840` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9860` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 50,550.00 USD | 3,630.00 USD | 24,750.00 USD |
| `7D` | `0.9860` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9880` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 17,200.00 USD | 151.21 USD | 14,320.00 USD |
| `7D` | `0.9880` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9900` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 11,850.00 USD |
| `7D` | `0.9900` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9920` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 9,580.00 USD | 4,160.00 USD | 21,170.00 USD |
| `7D` | `0.9920` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD |
| `1D` | `0.9940` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 25,660.00 USD | 10,700.00 USD | 1,870.00 USD |
| `7D` | `0.9940` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD |
| `1D` | `0.9960` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 18,530.00 USD | 1,480.00 USD | 7,450.00 USD |
| `7D` | `0.9960` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9980` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 53,500.00 USD | 10,730.00 USD | 15,870.00 USD |
| `7D` | `0.9980` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `1.00` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 60,090.00 USD | 23,090.00 USD | 6,760.00 USD |
| `7D` | `1.00` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,430.00 USD | 1,930.00 USD | 7,450.00 USD |
| `7D` | `1.00` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 10,110.00 USD | 9,550.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD |
| `1D` | `1.01` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 22,410.00 USD | 9,170.00 USD | 30,960.00 USD |
| `7D` | `1.01` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 12,560.00 USD | 17,230.00 USD | 971.85 USD |
| `7D` | `1.01` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 16,480.00 USD | 22,350.00 USD | 265.91 USD |
| `7D` | `1.01` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 6,250.00 USD | 5,790.00 USD | 21,570.00 USD |
| `7D` | `1.01` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.02` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 14,730.00 USD | 25,460.00 USD | 11,300.00 USD |
| `7D` | `1.02` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 23,750.00 USD | 4,210.00 USD | 22,530.00 USD |
| `7D` | `1.02` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 46,900.00 USD | 9,980.00 USD | 18,380.00 USD |
| `7D` | `1.02` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 40,340.00 USD | 21,340.00 USD | 29,140.00 USD |
| `7D` | `1.02` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 51,740.00 USD | 12,350.00 USD | 34,590.00 USD |
| `7D` | `1.02` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.03` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 40,090.00 USD | 18,290.00 USD | 21,370.00 USD |
| `7D` | `1.03` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 19,210.00 USD | 8,920.00 USD | 15,510.00 USD |
| `7D` | `1.03` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 64,370.00 USD | 12,650.00 USD | 18,360.00 USD |
| `7D` | `1.03` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 30,760.00 USD | 7,090.00 USD | 32,130.00 USD |
| `7D` | `1.03` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 12,440.00 USD | 8,670.00 USD | 12,980.00 USD |
| `7D` | `1.03` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.04` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 4,520.00 USD | 10,280.00 USD | 2,970.00 USD |
| `7D` | `1.04` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `1D` | `1.04` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 40,430.00 USD | 767.34 USD | 2,900.00 USD |
| `7D` | `1.04` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `1D` | `1.04` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 5,910.00 USD | 6,130.00 USD | 8,410.00 USD |
| `7D` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD |
| `1D` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 10,240.00 USD | 5,750.00 USD | 3,380.00 USD |
| `7D` | `1.04` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `1D` | `1.04` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 2,350.00 USD | 1,160.00 USD | 0.00 USD |
| `7D` | `1.04` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `7D` | `1.05` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `7D` | `1.05` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `7D` | `1.05` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `7D` | `1.05` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 141,110.00 USD | 49,780.00 USD | 134,080.00 USD |
| `7D` | `1.05` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD |
| `7D` | `1.06` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `7D` | `1.06` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 9,940,000.00 USD | 9,940,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD |
| `7D` | `1.06` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `7D` | `1.07` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD |
| `7D` | `1.07` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `7D` | `1.07` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD |
| `7D` | `1.07` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `7D` | `1.07` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD |
| `7D` | `1.08` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `7D` | `1.08` | 11,750,000.00 USD | 11,750,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `7D` | `1.08` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `7D` | `1.08` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD |
| `7D` | `1.08` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `7D` | `1.09` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD |
| `7D` | `1.09` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD |
| `7D` | `1.09` | 12,920,000.00 USD | 12,920,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `7D` | `1.09` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD |
| `7D` | `1.09` | 13,200,000.00 USD | 13,200,000.00 USD | 0.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD |
| `7D` | `1.10` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 66,380.00 USD | 32,080.00 USD | 65,790.00 USD |
| `7D` | `1.10` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD |
| `7D` | `1.10` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 182,190.00 USD | 62,380.00 USD | 40,340.00 USD |
| `7D` | `1.10` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 59,740.00 USD | 10,900.00 USD | 2,270.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `175.47M` | Total OI Tokens: `186,034,329.2 DOT`
  * 1h OI Change: `+0.31%` | 4h OI Change: `-6.78%` | 24h OI Change: `-16.48%`
  * Exchange Breakdown: Binance=`35.23M` | Bybit=`21.98M` | OKX=`10.30M` | Hyperliquid=`5.87M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `963.05` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0259%` |
| **USDT Bybit** | `-0.0007%` | **USDT KuCoin** | `-0.0157%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0007%` | **USDT Bitget** | `0.0054%` |
| **CoinM Binance** | `0.0035%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `48.04%` | `51.96%` | `0.92` | 20,750,000.00 USD |
| `15M` | `Binance` | `48.05%` | `51.95%` | `0.92` | 7,610,000.00 USD |
| `15M` | `OKX` | `31.55%` | `68.45%` | `0.46` | 2,570,000.00 USD |
| `15M` | `Bybit` | `55.24%` | `44.76%` | `1.23` | 3,050,000.00 USD |
| `15M` | `KuCoin` | `47.63%` | `52.37%` | `0.91` | 108,400.00 USD |
| `15M` | `Gate` | `69.02%` | `30.98%` | `2.23` | 2,920,000.00 USD |
| `15M` | `Bitget` | `43.6%` | `56.4%` | `0.77` | 888,010.00 USD |
| `15M` | `BingX` | `33.94%` | `66.06%` | `0.51` | 1,010,000.00 USD |
| `15M` | `MEXC` | `76.53%` | `23.47%` | `3.26` | 596,090.00 USD |
| `15M` | `Bitunix` | `49.95%` | `50.05%` | `1.00` | 416,070.00 USD |
| `15M` | `Hyperliquid` | `41.81%` | `58.19%` | `0.72` | 1,160,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.15%` | `48.85%` | `1.05` | 79,930.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 1,320.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 241,120.00 USD |
| `15M` | `HTX` | `42.45%` | `57.55%` | `0.74` | 7,470.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `74.43%` | `25.57%` | `2.91` | 20,300.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 76,070.00 USD |
| `15M` | `Whale Positions` | `48.05%` | `51.95%` | `0.92` | 7,610,000.00 USD |
| `15M` | `Global Accounts` | `48.04%` | `51.96%` | `0.92` | 20,750,000.00 USD |
| `1H` | `DOT` | `49.54%` | `50.46%` | `0.98` | 76,310,000.00 USD |
| `1H` | `Binance` | `50.38%` | `49.62%` | `1.02` | 31,680,000.00 USD |
| `1H` | `OKX` | `42.66%` | `57.34%` | `0.74` | 8,490,000.00 USD |
| `1H` | `Bybit` | `37.93%` | `62.07%` | `0.61` | 11,860,000.00 USD |
| `1H` | `KuCoin` | `48.26%` | `51.74%` | `0.93` | 406,670.00 USD |
| `1H` | `Gate` | `56.45%` | `43.55%` | `1.30` | 4,040,000.00 USD |
| `1H` | `Bitget` | `46.98%` | `53.02%` | `0.89` | 4,670,000.00 USD |
| `1H` | `BingX` | `45.98%` | `54.02%` | `0.85` | 3,640,000.00 USD |
| `1H` | `MEXC` | `66.58%` | `33.42%` | `1.99` | 2,830,000.00 USD |
| `1H` | `Bitunix` | `45.84%` | `54.16%` | `0.85` | 1,970,000.00 USD |
| `1H` | `Hyperliquid` | `40.35%` | `59.65%` | `0.68` | 4,610,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.68%` | `49.32%` | `1.03` | 383,510.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 4,310.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 1,080,000.00 USD |
| `1H` | `HTX` | `41.93%` | `58.07%` | `0.72` | 62,730.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `67.5%` | `32.5%` | `2.08` | 120,790.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 477,930.00 USD |
| `1H` | `Whale Positions` | `50.38%` | `49.62%` | `1.02` | 31,680,000.00 USD |
| `1H` | `Global Accounts` | `49.54%` | `50.46%` | `0.98` | 76,310,000.00 USD |
| `4H` | `DOT` | `54.98%` | `45.02%` | `1.22` | 324,770,000.00 USD |
| `4H` | `Binance` | `56.97%` | `43.03%` | `1.32` | 129,260,000.00 USD |
| `4H` | `OKX` | `56.32%` | `43.68%` | `1.29` | 39,120,000.00 USD |
| `4H` | `Bybit` | `54.98%` | `45.02%` | `1.22` | 41,480,000.00 USD |
| `4H` | `KuCoin` | `48.06%` | `51.94%` | `0.93` | 1,920,000.00 USD |
| `4H` | `Gate` | `59%` | `41%` | `1.44` | 17,170,000.00 USD |
| `4H` | `Bitget` | `51.41%` | `48.59%` | `1.06` | 18,030,000.00 USD |
| `4H` | `BingX` | `37.47%` | `62.53%` | `0.60` | 16,010,000.00 USD |
| `4H` | `MEXC` | `54.44%` | `45.56%` | `1.19` | 10,930,000.00 USD |
| `4H` | `Bitunix` | `49.83%` | `50.17%` | `0.99` | 6,510,000.00 USD |
| `4H` | `Hyperliquid` | `60.37%` | `39.63%` | `1.52` | 32,570,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.05%` | `50.95%` | `0.96` | 1,650,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 20,350.00 USD |
| `4H` | `WhiteBIT` | `99.84%` | `0.16%` | `624.00` | 5,400,000.00 USD |
| `4H` | `HTX` | `48.09%` | `51.91%` | `0.93` | 291,010.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.36%` | `54.64%` | `0.83` | 770,030.00 USD |
| `4H` | `Aster` | `14.93%` | `85.07%` | `0.18` | 2,090,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 1,540,000.00 USD |
| `4H` | `Whale Positions` | `56.97%` | `43.03%` | `1.32` | 129,260,000.00 USD |
| `4H` | `Global Accounts` | `54.98%` | `45.02%` | `1.22` | 324,770,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.9201` | `0.9176` | `0.9201` | `0.9222` | `0.9147` | 486,388.28 USD | 243,662.09 USD | 242,726.19 USD | 935.89 USD | `+0.19%` | `11B / 18S` |
| `0:00 UTC` | `0.9193` | `0.9207` | `0.9193` | `0.9244` | `0.9172` | 1,009,160.47 USD | 369,502.50 USD | 639,657.97 USD | -270,155.47 USD | `-26.77%` | `7B / 22S` |
| `5:00 UTC` | `0.9247` | `0.9214` | `0.9247` | `0.9264` | `0.9171` | 592,145.67 USD | 331,376.92 USD | 260,768.76 USD | 70,608.16 USD | `+11.92%` | `20B / 3S` |
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9314` | `0.9325` | `0.9344` | `0.9288` | 497,143.85 USD | 263,231.22 USD | 233,912.62 USD | 29,318.60 USD | `+5.90%` | `7B / 6S` |
| `0:00 UTC` | `0.9354` | `0.9348` | `0.9354` | `0.9365` | `0.9333` | 404,247.05 USD | 223,080.64 USD | 181,166.41 USD | 41,914.22 USD | `+10.37%` | `5B / 3S` |
| `5:00 UTC` | `0.9425` | `0.9411` | `0.9425` | `0.9454` | `0.9362` | 1,398,502.73 USD | 702,262.50 USD | 696,240.23 USD | 6,022.27 USD | `+0.43%` | `30B / 12S` |
| `0:00 UTC` | `0.9416` | `0.9422` | `0.9416` | `0.9434` | `0.9410` | 109,464.31 USD | 33,855.65 USD | 75,608.66 USD | -41,753.00 USD | `-38.14%` | `5B / 7S` |

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
| `5m` | -11,030.00 USD | -186,670.00 USD | **`DISTRIBUTION`** |
| `15m` | 45,210.00 USD | -215,160.00 USD | **`DISTRIBUTION`** |
| `30m` | 48,170.00 USD | -137,480.00 USD | **`DISTRIBUTION`** |
| `1h` | -5,960.00 USD | -248,710.00 USD | **`DISTRIBUTION`** |
| `2h` | 59,760.00 USD | 136,480.00 USD | **`ACCUMULATION`** |
| `4h` | 165,710.00 USD | 3,440,000.00 USD | **`ACCUMULATION`** |
| `6h` | -254,800.00 USD | 1,070,000.00 USD | **`ACCUMULATION`** |
| `8h` | 149,190.00 USD | -5,300,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,040,000.00 USD | -5,470,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,080,000.00 USD | -6,400,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,120,000.00 USD | -23,180,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,760,000.00 USD | -77,340,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.03K` | 15m=`+45.21K` | 1h=`-5.96K` | 24h=`-1.08M`
* Futures Capital Netflows: 5m=`-186.67K` | 15m=`-215.16K` | 1h=`-248.71K` | 24h=`-6.40M`
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
  * Execution Entry: `0.8938` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8511` (Risk Distance: `0.0427` pts)
  * +2.5R Take Profit: `1.00`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9253` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9680` (Risk Distance: `0.0427` pts)
  * +2.5R Take Profit: `0.8187`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9470`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
