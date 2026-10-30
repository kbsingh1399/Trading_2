# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:04:32 IST` (`2026-10-30 04:34:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.9220` | **Live Ask Quote**: `0.9420` | **Mid Price**: `0.9320`
- **Spread Points**: `20.00` | **Spread BPS**: `214.59 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.8934` | VWAP Z-Score: `+1.93` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0098` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `55.98` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9377` | Lower -3.00σ Band: `0.8492`
  * Upper +2.51σ Band: `0.9305` | Lower -2.51σ Band: `0.8564`
  * Upper +2.01σ Band: `0.9231` | Lower -2.01σ Band: `0.8638`
  * Upper +2.00σ Band: `0.9230` | Lower -2.00σ Band: `0.8639`
  * Upper +1.28σ Band: `0.9123` | Lower -1.28σ Band: `0.8745`
  * Upper +1.00σ Band: `0.9082` | Lower -1.00σ Band: `0.8787`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9141` | EMA-20=`0.9116` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9269` (Slope: `+0.0000`) | EMA-100=`0.9458`
  * Institutional Anchors: EMA-144=`0.9548` | EMA-200=`0.9617` (Slope: `-0.6795`) | EMA-233=`0.9658`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9226` (Distance: `+1.02%`)
  * Point of Control (POC) = `0.9112` (Distance: `+2.28%`)
  * Value Area Low (VAL) = `0.8932` (Distance: `+4.34%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9357` | Low=`0.9283`
  * New York Session (13:00-21:00 UTC): High=`0.9376` | Low=`0.9264`
  * Initial Balance (First Hour): IB High=`0.9348` | IB Low=`0.9292`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9283` - `0.9357`
  * Optimal Trade Entry (OTE 0.705): `0.9339`
  * Structural Invalidation Anchor (0.786): `0.9395`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9314` | `0.9329` | `0.9301` | `0.9310` | `174,145` | 162,209.49 USD | 42,113.20 USD | `+25.96%` | -3,990,934.55 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9310` | `0.9343` | `0.9308` | `0.9342` | `144,413` | 134,628.72 USD | 21,776.97 USD | `+16.18%` | -3,969,157.59 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9341` | `0.9341` | `0.9332` | `0.9334` | `16,491` | 15,395.35 USD | 4,201.60 USD | `+27.29%` | -3,964,955.99 USD | `+0.06` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9318` | `0.9327` | `0.9263` | `0.9308` | `565,610` | 525,506.21 USD | -2,547.17 USD | `-0.48%` | -4,037,989.51 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9308` | `0.9343` | `0.9288` | `0.9342` | `533,766` | 497,143.85 USD | 29,318.60 USD | `+5.90%` | -4,008,670.91 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9341` | `0.9341` | `0.9332` | `0.9336` | `18,034` | 16,836.58 USD | 5,642.83 USD | `+33.52%` | -4,003,028.08 USD | `-0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9068` | `0.9231` | `0.9022` | `0.9175` | `3,555,217` | 3,250,542.04 USD | 108,464.97 USD | `+3.34%` | -3,777,368.70 USD | `+0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9176` | `0.9341` | `0.9170` | `0.9318` | `3,070,214` | 2,839,814.60 USD | -92,909.79 USD | `-3.27%` | -3,870,278.49 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9318` | `0.9343` | `0.9263` | `0.9334` | `1,115,867` | 1,038,045.42 USD | 30,973.03 USD | `+2.98%` | -3,839,305.46 USD | `+0.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9343` | `0.9263` | `0.9334` | `1,115,867` | 1,038,045.42 USD | 30,973.03 USD | `+2.98%` | -3,976,946.22 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -92,512.40 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -889,577.85 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9343` | `0.9263` | `0.9334` | `1,115,867` | 1,038,045.42 USD | 30,973.03 USD | `+2.98%` | -3,976,946.22 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.9320`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.00` | 5,995.92 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 6.00K USD at 1.0033 USD [API] | `2026-10-29 01:20:22` |
| `ANNOUNCEMENT` | `INFO` | `1.00` | 5,995.91 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 6.00K USD at 1.0035 USD [API] | `2026-10-29 01:20:22` |
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
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 134,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 130,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 128,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 128,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,090,000.00 USD | 2,090,000.00 USD | 7,140.00 USD | 2,140.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 127,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7910` | 2,080,000.00 USD | 2,080,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 2,060,000.00 USD | 2,060,000.00 USD | 20,360.00 USD | 1,170.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 2,030,000.00 USD | 2,030,000.00 USD | 3,290.00 USD | 4,820.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 2,010,000.00 USD | 2,010,000.00 USD | 10,100.00 USD | 933.42 USD | 522.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 2,000,000.00 USD | 2,000,000.00 USD | 20,360.00 USD | 6,210.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 1,950,000.00 USD | 1,950,000.00 USD | 5,420.00 USD | 5,200.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8030` | 1,940,000.00 USD | 1,940,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 1,930,000.00 USD | 1,930,000.00 USD | 9,820.00 USD | 8,430.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,900,000.00 USD | 1,900,000.00 USD | 12,160.00 USD | 4,930.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,880,000.00 USD | 1,880,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,870,000.00 USD | 1,870,000.00 USD | 7,910.00 USD | 102.12 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,860,000.00 USD | 1,860,000.00 USD | 14,060.00 USD | 2,950.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 127,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,840,000.00 USD | 1,840,000.00 USD | 5,990.00 USD | 7,610.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,820,000.00 USD | 1,820,000.00 USD | 10,780.00 USD | 2,370.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,800,000.00 USD | 1,800,000.00 USD | 8,920.00 USD | 2,530.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,780,000.00 USD | 1,780,000.00 USD | 7,510.00 USD | 3,060.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 126,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,760,000.00 USD | 1,760,000.00 USD | 29,430.00 USD | 4,660.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 124,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8240` | 1,460,000.00 USD | 1,460,000.00 USD | 11,020.00 USD | 3,640.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8250` | 1,730,000.00 USD | 1,730,000.00 USD | 8,460.00 USD | 1,610.00 USD | 2,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8260` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 6,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8270` | 1,710,000.00 USD | 1,710,000.00 USD | 4,320.00 USD | 1,870.00 USD | 616.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8280` | 1,430,000.00 USD | 1,430,000.00 USD | 244.70 USD | 59.23 USD | 110.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8290` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 3,360.00 USD | 556.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8300` | 1,430,000.00 USD | 1,430,000.00 USD | 295.97 USD | 40.90 USD | 137.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8310` | 1,700,000.00 USD | 1,700,000.00 USD | 9,280.00 USD | 1,520.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8320` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 2,800.00 USD | 1,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8330` | 1,690,000.00 USD | 1,690,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8340` | 1,420,000.00 USD | 1,420,000.00 USD | 25,550.00 USD | 4,520.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8350` | 1,660,000.00 USD | 1,660,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8360` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 14,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 124,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,640,000.00 USD | 1,640,000.00 USD | 15,240.00 USD | 154.74 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 1,370,000.00 USD | 1,370,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 1,360,000.00 USD | 1,360,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,620,000.00 USD | 1,620,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 123,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,610,000.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,620.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 751.39 USD | 122,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 1,360,000.00 USD | 1,360,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,600,000.00 USD | 1,600,000.00 USD | 7,900.00 USD | 1,130.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,590,000.00 USD | 1,590,000.00 USD | 731.45 USD | 132.08 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 121,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 1,350,000.00 USD | 1,350,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,590,000.00 USD | 1,590,000.00 USD | 5,480.00 USD | 114.10 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 120,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,580,000.00 USD | 1,580,000.00 USD | 2,130.00 USD | 2,670.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 1,350,000.00 USD | 1,350,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,570,000.00 USD | 1,570,000.00 USD | 254.55 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,350,000.00 USD | 1,350,000.00 USD | 2,270.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 117,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 1,340,000.00 USD | 1,340,000.00 USD | 617.52 USD | 197.60 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 211.77 USD | 1,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 180.75 USD | 116,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8600` | 1,340,000.00 USD | 1,340,000.00 USD | 6,520.00 USD | 1,220.00 USD | 251.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,560,000.00 USD | 1,560,000.00 USD | 7,320.00 USD | 2,920.00 USD | 467.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 1,340,000.00 USD | 1,340,000.00 USD | 7,410.00 USD | 70.98 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,550,000.00 USD | 1,550,000.00 USD | 758.91 USD | 2,820.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 116,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,330,000.00 USD | 1,330,000.00 USD | 6,350.00 USD | 2,070.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,550,000.00 USD | 1,550,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,540,000.00 USD | 1,540,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,320,000.00 USD | 1,320,000.00 USD | 3,580.00 USD | 3,640.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,520,000.00 USD | 1,520,000.00 USD | 25,250.00 USD | 2,030.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,300,000.00 USD | 1,300,000.00 USD | 21,490.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,480,000.00 USD | 1,480,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 92,580.00 USD | 102,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,270,000.00 USD | 1,270,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,080.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,230,000.00 USD | 1,230,000.00 USD | 7,270.00 USD | 3,350.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 583.80 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,220,000.00 USD | 1,220,000.00 USD | 17,510.00 USD | 3,760.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,450,000.00 USD | 1,450,000.00 USD | 52,140.00 USD | 15,830.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,190,000.00 USD | 1,190,000.00 USD | 24,840.00 USD | 15,580.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,380,000.00 USD | 1,380,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,120,000.00 USD | 1,120,000.00 USD | 47,770.00 USD | 13,000.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,370,000.00 USD | 1,370,000.00 USD | 228.30 USD | 53.23 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,060,000.00 USD | 1,060,000.00 USD | 11,810.00 USD | 13,820.00 USD | 425.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,370,000.00 USD | 1,370,000.00 USD | 8,430.00 USD | 6,110.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,030,000.00 USD | 1,030,000.00 USD | 11,270.00 USD | 3,590.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8850` | 1,360,000.00 USD | 1,360,000.00 USD | 8,630.00 USD | 10,310.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8860` | 1,020,000.00 USD | 1,020,000.00 USD | 5,930.00 USD | 7,590.00 USD | 9,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8870` | 1,340,000.00 USD | 1,340,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8880` | 993,080.00 USD | 993,080.00 USD | 63,000.00 USD | 12,170.00 USD | 22,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8890` | 1,300,000.00 USD | 1,300,000.00 USD | 54,380.00 USD | 29,430.00 USD | 14,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8900` | 895,350.00 USD | 895,350.00 USD | 67,680.00 USD | 19,960.00 USD | 19,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8910` | 1,210,000.00 USD | 1,210,000.00 USD | 73,870.00 USD | 10,440.00 USD | 35,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8920` | 788,490.00 USD | 788,490.00 USD | 4,920.00 USD | 7,510.00 USD | 38,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8930` | 1,090,000.00 USD | 1,090,000.00 USD | 62,870.00 USD | 10,800.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8940` | 737,090.00 USD | 737,090.00 USD | 49,140.00 USD | 7,700.00 USD | 966.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8950` | 1,000,000.00 USD | 1,000,000.00 USD | 7,380.00 USD | 37,670.00 USD | 47,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8960` | 679,280.00 USD | 679,280.00 USD | 21,000.00 USD | 15,480.00 USD | 16,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8970` | 910,840.00 USD | 910,840.00 USD | 106,410.00 USD | 4,500.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8980` | 626,730.00 USD | 626,730.00 USD | 71,390.00 USD | 10,780.00 USD | 32,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8990` | 770,040.00 USD | 770,040.00 USD | 52,250.00 USD | 23,060.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9000` | 511,670.00 USD | 511,670.00 USD | 24,060.00 USD | 35,660.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9010` | 675,500.00 USD | 675,500.00 USD | 20,170.00 USD | 11,220.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9020` | 449,580.00 USD | 449,580.00 USD | 10,140.00 USD | 3,120.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9030` | 640,880.00 USD | 640,880.00 USD | 13,100.00 USD | 7,840.00 USD | 27,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9040` | 433,530.00 USD | 433,530.00 USD | 8,540.00 USD | 8,840.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9050` | 592,490.00 USD | 592,490.00 USD | 31,190.00 USD | 10,970.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9060` | 409,340.00 USD | 409,340.00 USD | 0.00 USD | 19,030.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9070` | 523,030.00 USD | 523,030.00 USD | 114,070.00 USD | 48,260.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9080` | 380,340.00 USD | 380,340.00 USD | 126,150.00 USD | 39,140.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9090` | 345,200.00 USD | 345,200.00 USD | 86,450.00 USD | 0.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9100` | 168,940.00 USD | 168,940.00 USD | 1,380.00 USD | 9,610.00 USD | 74,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9110` | 227,950.00 USD | 227,950.00 USD | 76,180.00 USD | 10,340.00 USD | 16,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9120` | 83,920.00 USD | 83,920.00 USD | 48,810.00 USD | 15,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9130` | 124,980.00 USD | 124,980.00 USD | 0.00 USD | 17,740.00 USD | 40,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9140` | 19,410.00 USD | 19,410.00 USD | 0.00 USD | 129.18 USD | 19,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9150` | 66,940.00 USD | 66,940.00 USD | 0.00 USD | 0.00 USD | 33,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9160` | 251.44 USD | 251.44 USD | 0.00 USD | 131.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9170` | 33,720.00 USD | 33,720.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9180` | 119.99 USD | 119.99 USD | 0.00 USD | 119.99 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9190` | 18,470.00 USD | 18,470.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 15,790.00 USD | 15,790.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9210` | 31,590.00 USD | 31,590.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9220` | 9,360.00 USD | 9,360.00 USD | 0.00 USD | 0.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9230` | 95,890.00 USD | 95,890.00 USD | 27,030.00 USD | 161.70 USD | 37,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9240` | 9,900.00 USD | 9,900.00 USD | 0.00 USD | 534.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9250` | 97,770.00 USD | 97,770.00 USD | 0.00 USD | 1,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9260` | 10,600.00 USD | 10,600.00 USD | 0.00 USD | 704.59 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9270` | 99,000.00 USD | 99,000.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9280` | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 145.20 USD | 353.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9290` | 100,000.00 USD | 100,000.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9300` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 221.69 USD | 753.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9310` | 100,920.00 USD | 100,920.00 USD | 0.00 USD | 916.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9320` | 59,300.00 USD | 59,300.00 USD | 32,020.00 USD | 7,580.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9330` | 102,340.00 USD | 102,340.00 USD | 0.00 USD | 1,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9340` | 156,390.00 USD | 156,390.00 USD | 85,190.00 USD | 10,860.00 USD | 1,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9350` | 104,670.00 USD | 104,670.00 USD | 0.00 USD | 1,560.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9360` | 296,160.00 USD | 296,160.00 USD | 84,420.00 USD | 35,410.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9370` | 124,180.00 USD | 124,180.00 USD | 16,340.00 USD | 1,410.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9380` | 359,320.00 USD | 359,320.00 USD | 61,800.00 USD | 103.28 USD | 1,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9390` | 177,000.00 USD | 177,000.00 USD | 39,250.00 USD | 3,930.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9400` | 418,140.00 USD | 418,140.00 USD | 48,690.00 USD | 6,410.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9410` | 226,890.00 USD | 226,890.00 USD | 29,630.00 USD | 13,070.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9420` | 503,000.00 USD | 503,000.00 USD | 57,470.00 USD | 17,410.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9430` | 286,430.00 USD | 286,430.00 USD | 45,490.00 USD | 1,530.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9440` | 677,290.00 USD | 677,290.00 USD | 149,360.00 USD | 7,300.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9450` | 668,810.00 USD | 668,810.00 USD | 261,930.00 USD | 49,360.00 USD | 71,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9460` | 818,290.00 USD | 818,290.00 USD | 80,840.00 USD | 31,690.00 USD | 28,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9470` | 947,640.00 USD | 947,640.00 USD | 200,510.00 USD | 1,720.00 USD | 76,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9480` | 1,060,000.00 USD | 1,060,000.00 USD | 155,950.00 USD | 8,800.00 USD | 74,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9490` | 1,330,000.00 USD | 1,330,000.00 USD | 193,040.00 USD | 11,450.00 USD | 178,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9500` | 1,180,000.00 USD | 1,180,000.00 USD | 107,250.00 USD | 15,500.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9510` | 1,720,000.00 USD | 1,720,000.00 USD | 242,000.00 USD | 29,060.00 USD | 117,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9520` | 1,290,000.00 USD | 1,290,000.00 USD | 47,190.00 USD | 13,390.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9530` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 3,430.00 USD | 121,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9540` | 1,370,000.00 USD | 1,370,000.00 USD | 43,540.00 USD | 7,980.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9550` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 20,780.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9560` | 1,380,000.00 USD | 1,380,000.00 USD | 3,730.00 USD | 9,750.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9570` | 1,890,000.00 USD | 1,890,000.00 USD | 1,910.00 USD | 6,700.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9580` | 1,390,000.00 USD | 1,390,000.00 USD | 3,480.00 USD | 1,660.00 USD | 313.25 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9590` | 1,900,000.00 USD | 1,900,000.00 USD | 1,980.00 USD | 5,170.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9600` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 5,890.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9610` | 1,930,000.00 USD | 1,930,000.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9620` | 1,470,000.00 USD | 1,470,000.00 USD | 51,380.00 USD | 8,170.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9630` | 2,000,000.00 USD | 2,000,000.00 USD | 53,510.00 USD | 24,130.00 USD | 481.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9640` | 1,540,000.00 USD | 1,540,000.00 USD | 17,560.00 USD | 25,430.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9650` | 2,070,000.00 USD | 2,070,000.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9660` | 1,580,000.00 USD | 1,580,000.00 USD | 2,450.00 USD | 4,670.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9670` | 2,110,000.00 USD | 2,110,000.00 USD | 38,090.00 USD | 5,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9680` | 1,610,000.00 USD | 1,610,000.00 USD | 24,830.00 USD | 7,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9690` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 19,330.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9695` | 14,720.00 USD | 14,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,680,000.00 USD | 1,680,000.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,180,000.00 USD | 2,180,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,730,000.00 USD | 1,730,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 214.00 USD | 14,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,810,000.00 USD | 1,810,000.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,300,000.00 USD | 2,300,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,870,000.00 USD | 1,870,000.00 USD | 39,980.00 USD | 3,080.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,930,000.00 USD | 1,930,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,510,000.00 USD | 2,510,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,960,000.00 USD | 1,960,000.00 USD | 16,350.00 USD | 12,360.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,680,000.00 USD | 2,680,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 2,010,000.00 USD | 2,010,000.00 USD | 665.59 USD | 13,370.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,000.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 2,090,000.00 USD | 2,090,000.00 USD | 50,550.00 USD | 3,510.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,800,000.00 USD | 2,800,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 2,120,000.00 USD | 2,120,000.00 USD | 17,200.00 USD | 130.81 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,820,000.00 USD | 2,820,000.00 USD | 20,530.00 USD | 284.26 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 2,190,000.00 USD | 2,190,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 2,220,000.00 USD | 2,220,000.00 USD | 9,210.00 USD | 2,900.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 2,240,000.00 USD | 2,240,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,920,000.00 USD | 2,920,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 2,270,000.00 USD | 2,270,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 3,000,000.00 USD | 3,000,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 2,320,000.00 USD | 2,320,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 104.05 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,050,000.00 USD | 3,050,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,200,000.00 USD | 3,200,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,440,000.00 USD | 2,440,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,230,000.00 USD | 3,230,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 15,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,300,000.00 USD | 3,300,000.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,640,000.00 USD | 2,640,000.00 USD | 20,230.00 USD | 9,160.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,320,000.00 USD | 3,320,000.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,670,000.00 USD | 2,670,000.00 USD | 10,530.00 USD | 15,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,360,000.00 USD | 3,360,000.00 USD | 20,090.00 USD | 14,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,710,000.00 USD | 2,710,000.00 USD | 16,480.00 USD | 25,410.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,410,000.00 USD | 3,410,000.00 USD | 16,020.00 USD | 35,070.00 USD | 388.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,750,000.00 USD | 2,750,000.00 USD | 6,250.00 USD | 4,410.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 26,360.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,790,000.00 USD | 2,790,000.00 USD | 20,120.00 USD | 2,880.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,490,000.00 USD | 3,490,000.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,850,000.00 USD | 2,850,000.00 USD | 24,880.00 USD | 8,530.00 USD | 25,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,600,000.00 USD | 3,600,000.00 USD | 16,530.00 USD | 83,630.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 2,930,000.00 USD | 2,930,000.00 USD | 52,040.00 USD | 8,850.00 USD | 20,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,770,000.00 USD | 3,770,000.00 USD | 61,450.00 USD | 33,450.00 USD | 68,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,020,000.00 USD | 3,020,000.00 USD | 51,380.00 USD | 3,710.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,080,000.00 USD | 4,080,000.00 USD | 82,230.00 USD | 85,290.00 USD | 146,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,160,000.00 USD | 3,160,000.00 USD | 59,910.00 USD | 27,540.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,190,000.00 USD | 4,190,000.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,250,000.00 USD | 3,250,000.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,510,000.00 USD | 4,510,000.00 USD | 161,070.00 USD | 126,870.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,320,000.00 USD | 3,320,000.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,720,000.00 USD | 4,720,000.00 USD | 142,240.00 USD | 39,320.00 USD | 30,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,470,000.00 USD | 3,470,000.00 USD | 95,330.00 USD | 24,510.00 USD | 33,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,920,000.00 USD | 4,920,000.00 USD | 170,960.00 USD | 11,060.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,570,000.00 USD | 3,570,000.00 USD | 65,270.00 USD | 8,900.00 USD | 29,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,050,000.00 USD | 5,050,000.00 USD | 122,910.00 USD | 0.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,610,000.00 USD | 3,610,000.00 USD | 16,660.00 USD | 9,110.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,360,000.00 USD | 5,360,000.00 USD | 259,060.00 USD | 8,490.00 USD | 43,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,660,000.00 USD | 5,660,000.00 USD | 192,080.00 USD | 4,020.00 USD | 109,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 15,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,030,000.00 USD | 6,030,000.00 USD | 239,580.00 USD | 8,210.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,930,000.00 USD | 6,930,000.00 USD | 184,670.00 USD | 23,680.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,450,000.00 USD | 7,450,000.00 USD | 178,890.00 USD | 96,750.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 15,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,650,000.00 USD | 7,650,000.00 USD | 116,670.00 USD | 13,190.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,960,000.00 USD | 7,960,000.00 USD | 175,350.00 USD | 43,000.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,160,000.00 USD | 8,160,000.00 USD | 68,590.00 USD | 58,720.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,390,000.00 USD | 8,390,000.00 USD | 125,020.00 USD | 33,480.00 USD | 72,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 8,790,000.00 USD | 8,790,000.00 USD | 218,860.00 USD | 71,040.00 USD | 106,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,250,000.00 USD | 9,250,000.00 USD | 240,060.00 USD | 74,400.00 USD | 145,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,520,000.00 USD | 9,520,000.00 USD | 140,850.00 USD | 57,130.00 USD | 78,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,810,000.00 USD | 9,810,000.00 USD | 141,700.00 USD | 72,850.00 USD | 71,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 10,020,000.00 USD | 10,020,000.00 USD | 90,670.00 USD | 28,820.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,240,000.00 USD | 10,240,000.00 USD | 86,760.00 USD | 43,510.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,540,000.00 USD | 10,540,000.00 USD | 219,670.00 USD | 15,540.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,760,000.00 USD | 10,760,000.00 USD | 141,570.00 USD | 35,440.00 USD | 52,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,000,000.00 USD | 11,000,000.00 USD | 96,630.00 USD | 43,620.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,190,000.00 USD | 11,190,000.00 USD | 97,650.00 USD | 27,650.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,340,000.00 USD | 11,340,000.00 USD | 75,040.00 USD | 29,740.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,580,000.00 USD | 11,580,000.00 USD | 166,380.00 USD | 21,770.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,810,000.00 USD | 11,810,000.00 USD | 164,440.00 USD | 26,210.00 USD | 33,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 17,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,010,000.00 USD | 12,010,000.00 USD | 61,330.00 USD | 40,620.00 USD | 100,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,160,000.00 USD | 12,160,000.00 USD | 86,400.00 USD | 18,560.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,390,000.00 USD | 12,390,000.00 USD | 102,510.00 USD | 58,250.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,570,000.00 USD | 12,570,000.00 USD | 71,650.00 USD | 23,780.00 USD | 85,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,700,000.00 USD | 12,700,000.00 USD | 70,660.00 USD | 25,310.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,860,000.00 USD | 12,860,000.00 USD | 59,760.00 USD | 39,810.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,030,000.00 USD | 13,030,000.00 USD | 54,830.00 USD | 23,050.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,180,000.00 USD | 13,180,000.00 USD | 92,660.00 USD | 13,440.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,500,000.00 USD | 13,500,000.00 USD | 188,000.00 USD | 48,960.00 USD | 89,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,680,000.00 USD | 13,680,000.00 USD | 122,300.00 USD | 43,950.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,910,000.00 USD | 13,910,000.00 USD | 91,720.00 USD | 19,120.00 USD | 110,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,970,000.00 USD | 13,970,000.00 USD | 22,500.00 USD | 10,330.00 USD | 31,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,080,000.00 USD | 14,080,000.00 USD | 51,840.00 USD | 24,560.00 USD | 34,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,260,000.00 USD | 14,260,000.00 USD | 80,930.00 USD | 42,090.00 USD | 56,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 18,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,420,000.00 USD | 14,420,000.00 USD | 77,150.00 USD | 18,170.00 USD | 64,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,520,000.00 USD | 14,520,000.00 USD | 28,830.00 USD | 43,670.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.11` | 14,570,000.00 USD | 14,570,000.00 USD | 32,810.00 USD | 5,830.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,720,000.00 USD | 14,720,000.00 USD | 75,790.00 USD | 45,850.00 USD | 32,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,780,000.00 USD | 14,780,000.00 USD | 24,700.00 USD | 23,340.00 USD | 13,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,890,000.00 USD | 14,890,000.00 USD | 49,110.00 USD | 31,670.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 14,980,000.00 USD | 14,980,000.00 USD | 61,780.00 USD | 6,470.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.12` | 15,040,000.00 USD | 15,040,000.00 USD | 18,300.00 USD | 10,300.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,060,000.00 USD | 15,060,000.00 USD | 14,700.00 USD | 1,030.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,170,000.00 USD | 15,170,000.00 USD | 46,320.00 USD | 10,950.00 USD | 45,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,360,000.00 USD | 15,360,000.00 USD | 95,750.00 USD | 12,720.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.13` | 15,460,000.00 USD | 15,460,000.00 USD | 66,770.00 USD | 3,820.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,550,000.00 USD | 15,550,000.00 USD | 16,300.00 USD | 10,520.00 USD | 61,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,570,000.00 USD | 15,570,000.00 USD | 4,780.00 USD | 5,350.00 USD | 6,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,600,000.00 USD | 15,600,000.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,660,000.00 USD | 15,660,000.00 USD | 36,300.00 USD | 8,930.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.14` | 15,730,000.00 USD | 15,730,000.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.7890` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 7,140.00 USD | 2,140.00 USD | 2,800.00 USD |
| `7D` | `0.7910` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD |
| `7D` | `0.7930` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 20,360.00 USD | 1,170.00 USD | 6,130.00 USD |
| `7D` | `0.7950` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 3,290.00 USD | 4,820.00 USD | 14,710.00 USD |
| `7D` | `0.7970` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 10,100.00 USD | 933.42 USD | 522.30 USD |
| `7D` | `0.7990` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 20,360.00 USD | 6,210.00 USD | 13,950.00 USD |
| `7D` | `0.8010` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 5,420.00 USD | 5,200.00 USD | 2,300.00 USD |
| `7D` | `0.8030` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD |
| `7D` | `0.8050` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 9,820.00 USD | 8,430.00 USD | 3,720.00 USD |
| `7D` | `0.8070` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 12,160.00 USD | 4,930.00 USD | 6,450.00 USD |
| `7D` | `0.8090` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD |
| `7D` | `0.8110` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 7,910.00 USD | 102.12 USD | 340.33 USD |
| `7D` | `0.8130` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 14,060.00 USD | 2,950.00 USD | 8,560.00 USD |
| `7D` | `0.8150` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 5,990.00 USD | 7,610.00 USD | 4,220.00 USD |
| `7D` | `0.8170` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 10,780.00 USD | 2,370.00 USD | 9,670.00 USD |
| `7D` | `0.8190` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 8,920.00 USD | 2,530.00 USD | 4,080.00 USD |
| `7D` | `0.8210` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 7,510.00 USD | 3,060.00 USD | 10,030.00 USD |
| `1D` | `0.8220` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD |
| `7D` | `0.8230` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 29,430.00 USD | 4,660.00 USD | 1,960.00 USD |
| `1D` | `0.8240` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 11,020.00 USD | 3,640.00 USD | 6,790.00 USD |
| `7D` | `0.8250` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 8,460.00 USD | 1,610.00 USD | 2,110.00 USD |
| `1D` | `0.8260` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 6,990.00 USD | 0.00 USD |
| `7D` | `0.8270` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 4,320.00 USD | 1,870.00 USD | 616.76 USD |
| `1D` | `0.8280` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 244.70 USD | 59.23 USD | 110.11 USD |
| `7D` | `0.8290` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 0.00 USD | 3,360.00 USD | 556.14 USD |
| `1D` | `0.8300` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 295.97 USD | 40.90 USD | 137.17 USD |
| `7D` | `0.8310` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 9,280.00 USD | 1,520.00 USD | 2,450.00 USD |
| `1D` | `0.8320` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 2,800.00 USD | 1,900.00 USD |
| `7D` | `0.8330` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 16,220.00 USD | 10,960.00 USD | 77.95 USD |
| `1D` | `0.8340` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 25,550.00 USD | 4,520.00 USD | 8,980.00 USD |
| `7D` | `0.8350` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 19,490.00 USD | 0.00 USD | 2,290.00 USD |
| `1D` | `0.8360` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 14,810.00 USD |
| `7D` | `0.8370` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 15,240.00 USD | 154.74 USD | 0.00 USD |
| `1D` | `0.8380` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD |
| `7D` | `0.8390` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD |
| `1D` | `0.8400` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8410` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD |
| `1D` | `0.8420` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD |
| `7D` | `0.8430` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,620.00 USD | 4,060.00 USD |
| `1D` | `0.8440` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8450` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 474.61 USD |
| `7D` | `0.8470` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 7,900.00 USD | 1,130.00 USD | 2,180.00 USD |
| `7D` | `0.8490` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 731.45 USD | 132.08 USD | 0.00 USD |
| `1D` | `0.8500` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD |
| `7D` | `0.8510` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 5,480.00 USD | 114.10 USD | 4,660.00 USD |
| `1D` | `0.8520` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD |
| `7D` | `0.8530` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 2,130.00 USD | 2,670.00 USD | 1,160.00 USD |
| `1D` | `0.8540` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.8550` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 254.55 USD | 0.00 USD | 4,380.00 USD |
| `1D` | `0.8560` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 2,270.00 USD | 199.60 USD | 0.00 USD |
| `7D` | `0.8570` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD |
| `1D` | `0.8580` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 617.52 USD | 197.60 USD | 182.69 USD |
| `7D` | `0.8590` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 0.00 USD | 211.77 USD | 1,270.00 USD |
| `1D` | `0.8600` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 6,520.00 USD | 1,220.00 USD | 251.39 USD |
| `7D` | `0.8610` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 7,320.00 USD | 2,920.00 USD | 467.14 USD |
| `1D` | `0.8620` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 7,410.00 USD | 70.98 USD | 0.00 USD |
| `7D` | `0.8630` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 758.91 USD | 2,820.00 USD | 1,280.00 USD |
| `1D` | `0.8640` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 6,350.00 USD | 2,070.00 USD | 3,790.00 USD |
| `7D` | `0.8650` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD |
| `1D` | `0.8660` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD |
| `7D` | `0.8670` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD |
| `1D` | `0.8680` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 3,580.00 USD | 3,640.00 USD | 8,720.00 USD |
| `7D` | `0.8690` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 25,250.00 USD | 2,030.00 USD | 8,040.00 USD |
| `1D` | `0.8700` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 21,490.00 USD | 3,580.00 USD | 4,760.00 USD |
| `7D` | `0.8710` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD |
| `1D` | `0.8720` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD |
| `7D` | `0.8730` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 2,080.00 USD | 295.31 USD |
| `1D` | `0.8740` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 7,270.00 USD | 3,350.00 USD | 3,030.00 USD |
| `7D` | `0.8750` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 583.80 USD | 6,210.00 USD |
| `1D` | `0.8760` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 17,510.00 USD | 3,760.00 USD | 4,390.00 USD |
| `7D` | `0.8770` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 52,140.00 USD | 15,830.00 USD | 2,760.00 USD |
| `1D` | `0.8780` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 24,840.00 USD | 15,580.00 USD | 27,090.00 USD |
| `7D` | `0.8790` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD |
| `1D` | `0.8800` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 47,770.00 USD | 13,000.00 USD | 5,490.00 USD |
| `7D` | `0.8810` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 228.30 USD | 53.23 USD | 0.00 USD |
| `1D` | `0.8820` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 11,810.00 USD | 13,820.00 USD | 425.40 USD |
| `7D` | `0.8830` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 8,430.00 USD | 6,110.00 USD | 957.94 USD |
| `1D` | `0.8840` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 11,270.00 USD | 3,590.00 USD | 1,030.00 USD |
| `7D` | `0.8850` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 8,630.00 USD | 10,310.00 USD | 866.69 USD |
| `1D` | `0.8860` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 5,930.00 USD | 7,590.00 USD | 9,740.00 USD |
| `7D` | `0.8870` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 19,060.00 USD | 5,060.00 USD | 7,460.00 USD |
| `1D` | `0.8880` | 993,080.00 USD | 0.00 USD | 993,080.00 USD | 63,000.00 USD | 12,170.00 USD | 22,560.00 USD |
| `7D` | `0.8890` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 54,380.00 USD | 29,430.00 USD | 14,360.00 USD |
| `1D` | `0.8900` | 895,350.00 USD | 0.00 USD | 895,350.00 USD | 67,680.00 USD | 19,960.00 USD | 19,230.00 USD |
| `7D` | `0.8910` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 73,870.00 USD | 10,440.00 USD | 35,050.00 USD |
| `1D` | `0.8920` | 788,490.00 USD | 0.00 USD | 788,490.00 USD | 4,920.00 USD | 7,510.00 USD | 38,970.00 USD |
| `7D` | `0.8930` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 62,870.00 USD | 10,800.00 USD | 10,100.00 USD |
| `1D` | `0.8940` | 737,090.00 USD | 0.00 USD | 737,090.00 USD | 49,140.00 USD | 7,700.00 USD | 966.50 USD |
| `7D` | `0.8950` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 7,380.00 USD | 37,670.00 USD | 47,060.00 USD |
| `1D` | `0.8960` | 679,280.00 USD | 0.00 USD | 679,280.00 USD | 21,000.00 USD | 15,480.00 USD | 16,060.00 USD |
| `7D` | `0.8970` | 910,840.00 USD | 0.00 USD | 910,840.00 USD | 106,410.00 USD | 4,500.00 USD | 29,890.00 USD |
| `1D` | `0.8980` | 626,730.00 USD | 0.00 USD | 626,730.00 USD | 71,390.00 USD | 10,780.00 USD | 32,910.00 USD |
| `7D` | `0.8990` | 770,040.00 USD | 0.00 USD | 770,040.00 USD | 52,250.00 USD | 23,060.00 USD | 19,220.00 USD |
| `1D` | `0.9000` | 511,670.00 USD | 0.00 USD | 511,670.00 USD | 24,060.00 USD | 35,660.00 USD | 2,370.00 USD |
| `7D` | `0.9010` | 675,500.00 USD | 0.00 USD | 675,500.00 USD | 20,170.00 USD | 11,220.00 USD | 3,230.00 USD |
| `1D` | `0.9020` | 449,580.00 USD | 0.00 USD | 449,580.00 USD | 10,140.00 USD | 3,120.00 USD | 2,790.00 USD |
| `7D` | `0.9030` | 640,880.00 USD | 0.00 USD | 640,880.00 USD | 13,100.00 USD | 7,840.00 USD | 27,460.00 USD |
| `1D` | `0.9040` | 433,530.00 USD | 0.00 USD | 433,530.00 USD | 8,540.00 USD | 8,840.00 USD | 6,810.00 USD |
| `7D` | `0.9050` | 592,490.00 USD | 0.00 USD | 592,490.00 USD | 31,190.00 USD | 10,970.00 USD | 27,300.00 USD |
| `1D` | `0.9060` | 409,340.00 USD | 0.00 USD | 409,340.00 USD | 0.00 USD | 19,030.00 USD | 9,970.00 USD |
| `7D` | `0.9070` | 523,030.00 USD | 0.00 USD | 523,030.00 USD | 114,070.00 USD | 48,260.00 USD | 15,500.00 USD |
| `1D` | `0.9080` | 380,340.00 USD | 0.00 USD | 380,340.00 USD | 126,150.00 USD | 39,140.00 USD | 46,100.00 USD |
| `7D` | `0.9090` | 345,200.00 USD | 0.00 USD | 345,200.00 USD | 86,450.00 USD | 0.00 USD | 30,800.00 USD |
| `1D` | `0.9100` | 168,940.00 USD | 0.00 USD | 168,940.00 USD | 1,380.00 USD | 9,610.00 USD | 74,030.00 USD |
| `7D` | `0.9110` | 227,950.00 USD | 0.00 USD | 227,950.00 USD | 76,180.00 USD | 10,340.00 USD | 16,450.00 USD |
| `1D` | `0.9120` | 83,920.00 USD | 0.00 USD | 83,920.00 USD | 48,810.00 USD | 15,700.00 USD | 0.00 USD |
| `7D` | `0.9130` | 124,980.00 USD | 0.00 USD | 124,980.00 USD | 0.00 USD | 17,740.00 USD | 40,290.00 USD |
| `1D` | `0.9140` | 19,410.00 USD | 0.00 USD | 19,410.00 USD | 0.00 USD | 129.18 USD | 19,030.00 USD |
| `7D` | `0.9150` | 66,940.00 USD | 0.00 USD | 66,940.00 USD | 0.00 USD | 0.00 USD | 33,220.00 USD |
| `1D` | `0.9160` | 251.44 USD | 0.00 USD | 251.44 USD | 0.00 USD | 131.45 USD | 0.00 USD |
| `7D` | `0.9170` | 33,720.00 USD | 0.00 USD | 33,720.00 USD | 0.00 USD | 0.00 USD | 15,250.00 USD |
| `1D` | `0.9180` | 119.99 USD | 0.00 USD | 119.99 USD | 0.00 USD | 119.99 USD | 0.00 USD |
| `7D` | `0.9190` | 18,470.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD | 0.00 USD | 18,470.00 USD |
| `1D` | `0.9210` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9210` | 15,790.00 USD | 15,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD |
| `7D` | `0.9210` | 31,590.00 USD | 31,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15,790.00 USD |
| `1D` | `0.9220` | 9,360.00 USD | 9,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,360.00 USD |
| `7D` | `0.9230` | 95,890.00 USD | 95,890.00 USD | 0.00 USD | 27,030.00 USD | 161.70 USD | 37,100.00 USD |
| `1D` | `0.9240` | 9,900.00 USD | 9,900.00 USD | 0.00 USD | 0.00 USD | 534.40 USD | 0.00 USD |
| `7D` | `0.9250` | 97,770.00 USD | 97,770.00 USD | 0.00 USD | 0.00 USD | 1,880.00 USD | 0.00 USD |
| `1D` | `0.9260` | 10,600.00 USD | 10,600.00 USD | 0.00 USD | 0.00 USD | 704.59 USD | 0.00 USD |
| `7D` | `0.9270` | 99,000.00 USD | 99,000.00 USD | 0.00 USD | 0.00 USD | 1,230.00 USD | 0.00 USD |
| `1D` | `0.9280` | 11,100.00 USD | 11,100.00 USD | 0.00 USD | 0.00 USD | 145.20 USD | 353.46 USD |
| `7D` | `0.9290` | 100,000.00 USD | 100,000.00 USD | 0.00 USD | 0.00 USD | 1,000.00 USD | 0.00 USD |
| `1D` | `0.9300` | 12,070.00 USD | 12,070.00 USD | 0.00 USD | 0.00 USD | 221.69 USD | 753.09 USD |
| `7D` | `0.9310` | 100,920.00 USD | 100,920.00 USD | 0.00 USD | 0.00 USD | 916.70 USD | 0.00 USD |
| `1D` | `0.9320` | 59,300.00 USD | 59,300.00 USD | 0.00 USD | 32,020.00 USD | 7,580.00 USD | 7,630.00 USD |
| `7D` | `0.9330` | 102,340.00 USD | 102,340.00 USD | 0.00 USD | 0.00 USD | 1,430.00 USD | 0.00 USD |
| `1D` | `0.9340` | 156,390.00 USD | 156,390.00 USD | 0.00 USD | 85,190.00 USD | 10,860.00 USD | 1,050.00 USD |
| `7D` | `0.9350` | 104,670.00 USD | 104,670.00 USD | 0.00 USD | 0.00 USD | 1,560.00 USD | 768.64 USD |
| `1D` | `0.9360` | 296,160.00 USD | 296,160.00 USD | 0.00 USD | 84,420.00 USD | 35,410.00 USD | 19,940.00 USD |
| `7D` | `0.9370` | 124,180.00 USD | 124,180.00 USD | 0.00 USD | 16,340.00 USD | 1,410.00 USD | 1,760.00 USD |
| `1D` | `0.9380` | 359,320.00 USD | 359,320.00 USD | 0.00 USD | 61,800.00 USD | 103.28 USD | 1,250.00 USD |
| `7D` | `0.9390` | 177,000.00 USD | 177,000.00 USD | 0.00 USD | 39,250.00 USD | 3,930.00 USD | 9,650.00 USD |
| `1D` | `0.9400` | 418,140.00 USD | 418,140.00 USD | 0.00 USD | 48,690.00 USD | 6,410.00 USD | 3,720.00 USD |
| `7D` | `0.9410` | 226,890.00 USD | 226,890.00 USD | 0.00 USD | 29,630.00 USD | 13,070.00 USD | 7,180.00 USD |
| `1D` | `0.9420` | 503,000.00 USD | 503,000.00 USD | 0.00 USD | 57,470.00 USD | 17,410.00 USD | 9,970.00 USD |
| `7D` | `0.9430` | 286,430.00 USD | 286,430.00 USD | 0.00 USD | 45,490.00 USD | 1,530.00 USD | 12,520.00 USD |
| `1D` | `0.9440` | 677,290.00 USD | 677,290.00 USD | 0.00 USD | 149,360.00 USD | 7,300.00 USD | 17,630.00 USD |
| `7D` | `0.9450` | 668,810.00 USD | 668,810.00 USD | 0.00 USD | 261,930.00 USD | 49,360.00 USD | 71,090.00 USD |
| `1D` | `0.9460` | 818,290.00 USD | 818,290.00 USD | 0.00 USD | 80,840.00 USD | 31,690.00 USD | 28,470.00 USD |
| `7D` | `0.9470` | 947,640.00 USD | 947,640.00 USD | 0.00 USD | 200,510.00 USD | 1,720.00 USD | 76,590.00 USD |
| `1D` | `0.9480` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 155,950.00 USD | 8,800.00 USD | 74,030.00 USD |
| `7D` | `0.9490` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 193,040.00 USD | 11,450.00 USD | 178,870.00 USD |
| `1D` | `0.9500` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 107,250.00 USD | 15,500.00 USD | 2,230.00 USD |
| `7D` | `0.9510` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 242,000.00 USD | 29,060.00 USD | 117,190.00 USD |
| `1D` | `0.9520` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 47,190.00 USD | 13,390.00 USD | 44,330.00 USD |
| `7D` | `0.9530` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 3,430.00 USD | 121,100.00 USD |
| `1D` | `0.9540` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 43,540.00 USD | 7,980.00 USD | 29,110.00 USD |
| `7D` | `0.9550` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 20,780.00 USD | 18,890.00 USD |
| `1D` | `0.9560` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 3,730.00 USD | 9,750.00 USD | 275.27 USD |
| `7D` | `0.9570` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 1,910.00 USD | 6,700.00 USD | 957.94 USD |
| `1D` | `0.9580` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 3,480.00 USD | 1,660.00 USD | 313.25 USD |
| `7D` | `0.9590` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 1,980.00 USD | 5,170.00 USD | 866.69 USD |
| `1D` | `0.9600` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 1,550.00 USD |
| `7D` | `0.9610` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 24,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9620` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 51,380.00 USD | 8,170.00 USD | 12,810.00 USD |
| `7D` | `0.9630` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 53,510.00 USD | 24,130.00 USD | 481.70 USD |
| `1D` | `0.9640` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 17,560.00 USD | 25,430.00 USD | 27,630.00 USD |
| `7D` | `0.9650` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 51,500.00 USD | 0.00 USD | 12,330.00 USD |
| `1D` | `0.9660` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 2,450.00 USD | 4,670.00 USD | 37,020.00 USD |
| `7D` | `0.9670` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 38,090.00 USD | 5,450.00 USD | 0.00 USD |
| `1D` | `0.9680` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 24,830.00 USD | 7,940.00 USD | 0.00 USD |
| `7D` | `0.9690` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 19,330.00 USD | 20,150.00 USD |
| `1D` | `0.9700` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD |
| `7D` | `0.9710` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD |
| `1D` | `0.9720` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD |
| `7D` | `0.9730` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD |
| `1D` | `0.9740` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD |
| `7D` | `0.9750` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD |
| `1D` | `0.9760` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD |
| `7D` | `0.9770` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD |
| `1D` | `0.9780` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 39,980.00 USD | 3,080.00 USD | 17,920.00 USD |
| `7D` | `0.9790` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD |
| `1D` | `0.9800` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD |
| `7D` | `0.9810` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD |
| `1D` | `0.9820` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 16,350.00 USD | 12,360.00 USD | 6,870.00 USD |
| `7D` | `0.9830` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD |
| `1D` | `0.9840` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 665.59 USD | 13,370.00 USD | 38,710.00 USD |
| `7D` | `0.9850` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 1,000.00 USD | 22,300.00 USD |
| `1D` | `0.9860` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 50,550.00 USD | 3,510.00 USD | 19,890.00 USD |
| `7D` | `0.9870` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `0.9880` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 17,200.00 USD | 130.81 USD | 14,320.00 USD |
| `7D` | `0.9890` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 20,530.00 USD | 284.26 USD | 1,440.00 USD |
| `1D` | `0.9900` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD |
| `7D` | `0.9910` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD |
| `1D` | `0.9920` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 9,210.00 USD | 2,900.00 USD | 13,340.00 USD |
| `7D` | `0.9930` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `0.9940` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD |
| `7D` | `0.9950` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD |
| `1D` | `0.9960` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD |
| `7D` | `0.9970` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD |
| `1D` | `0.9980` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD |
| `7D` | `0.9990` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 104.05 USD | 462.12 USD |
| `1D` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD |
| `7D` | `1.00` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 501.30 USD | 0.00 USD | 266.05 USD |
| `7D` | `1.00` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD |
| `7D` | `1.00` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD |
| `7D` | `1.01` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 34,110.00 USD | 0.00 USD | 29,210.00 USD |
| `1D` | `1.01` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 20,230.00 USD | 9,160.00 USD | 27,730.00 USD |
| `7D` | `1.01` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 15,500.00 USD |
| `1D` | `1.01` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 10,530.00 USD | 15,780.00 USD | 0.00 USD |
| `7D` | `1.01` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 20,090.00 USD | 14,020.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 16,480.00 USD | 25,410.00 USD | 265.91 USD |
| `7D` | `1.01` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 16,020.00 USD | 35,070.00 USD | 388.43 USD |
| `1D` | `1.01` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 6,250.00 USD | 4,410.00 USD | 25,160.00 USD |
| `7D` | `1.01` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 26,360.00 USD | 7,420.00 USD |
| `1D` | `1.02` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 20,120.00 USD | 2,880.00 USD | 22,170.00 USD |
| `7D` | `1.02` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 526.60 USD | 21,770.00 USD | 26,400.00 USD |
| `1D` | `1.02` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 24,880.00 USD | 8,530.00 USD | 25,750.00 USD |
| `7D` | `1.02` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 16,530.00 USD | 83,630.00 USD | 11,810.00 USD |
| `1D` | `1.02` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 52,040.00 USD | 8,850.00 USD | 20,560.00 USD |
| `7D` | `1.02` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 61,450.00 USD | 33,450.00 USD | 68,370.00 USD |
| `1D` | `1.02` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 51,380.00 USD | 3,710.00 USD | 36,250.00 USD |
| `7D` | `1.02` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 82,230.00 USD | 85,290.00 USD | 146,060.00 USD |
| `1D` | `1.02` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 59,910.00 USD | 27,540.00 USD | 53,210.00 USD |
| `7D` | `1.02` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 28,320.00 USD | 48,490.00 USD | 37,230.00 USD |
| `1D` | `1.03` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 52,630.00 USD | 18,370.00 USD | 20,210.00 USD |
| `7D` | `1.03` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 161,070.00 USD | 126,870.00 USD | 25,260.00 USD |
| `1D` | `1.03` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 31,340.00 USD | 10,940.00 USD | 18,480.00 USD |
| `7D` | `1.03` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 142,240.00 USD | 39,320.00 USD | 30,660.00 USD |
| `1D` | `1.03` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 95,330.00 USD | 24,510.00 USD | 33,580.00 USD |
| `7D` | `1.03` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 170,960.00 USD | 11,060.00 USD | 19,590.00 USD |
| `1D` | `1.03` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 65,270.00 USD | 8,900.00 USD | 29,750.00 USD |
| `7D` | `1.03` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 122,910.00 USD | 0.00 USD | 3,750.00 USD |
| `1D` | `1.03` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 16,660.00 USD | 9,110.00 USD | 13,850.00 USD |
| `7D` | `1.03` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 259,060.00 USD | 8,490.00 USD | 43,490.00 USD |
| `7D` | `1.04` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 192,080.00 USD | 4,020.00 USD | 109,460.00 USD |
| `7D` | `1.04` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 239,580.00 USD | 8,210.00 USD | 117,630.00 USD |
| `7D` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD |
| `7D` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD |
| `7D` | `1.04` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 184,670.00 USD | 23,680.00 USD | 59,810.00 USD |
| `7D` | `1.05` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 178,890.00 USD | 96,750.00 USD | 238,570.00 USD |
| `7D` | `1.05` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 116,670.00 USD | 13,190.00 USD | 77,320.00 USD |
| `7D` | `1.05` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 175,350.00 USD | 43,000.00 USD | 87,370.00 USD |
| `7D` | `1.05` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 68,590.00 USD | 58,720.00 USD | 74,380.00 USD |
| `7D` | `1.05` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 125,020.00 USD | 33,480.00 USD | 72,330.00 USD |
| `7D` | `1.06` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 218,860.00 USD | 71,040.00 USD | 106,380.00 USD |
| `7D` | `1.06` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 240,060.00 USD | 74,400.00 USD | 145,470.00 USD |
| `7D` | `1.06` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 140,850.00 USD | 57,130.00 USD | 78,020.00 USD |
| `7D` | `1.06` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 141,700.00 USD | 72,850.00 USD | 71,340.00 USD |
| `7D` | `1.06` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 90,670.00 USD | 28,820.00 USD | 95,080.00 USD |
| `7D` | `1.07` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 86,760.00 USD | 43,510.00 USD | 82,980.00 USD |
| `7D` | `1.07` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 219,670.00 USD | 15,540.00 USD | 62,270.00 USD |
| `7D` | `1.07` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 141,570.00 USD | 35,440.00 USD | 52,290.00 USD |
| `7D` | `1.07` | 11,000,000.00 USD | 11,000,000.00 USD | 0.00 USD | 96,630.00 USD | 43,620.00 USD | 95,510.00 USD |
| `7D` | `1.07` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 97,650.00 USD | 27,650.00 USD | 60,670.00 USD |
| `7D` | `1.08` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 75,040.00 USD | 29,740.00 USD | 48,910.00 USD |
| `7D` | `1.08` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 166,380.00 USD | 21,770.00 USD | 52,480.00 USD |
| `7D` | `1.08` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 164,440.00 USD | 26,210.00 USD | 33,950.00 USD |
| `7D` | `1.08` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 61,330.00 USD | 40,620.00 USD | 100,750.00 USD |
| `7D` | `1.08` | 12,160,000.00 USD | 12,160,000.00 USD | 0.00 USD | 86,400.00 USD | 18,560.00 USD | 46,440.00 USD |
| `7D` | `1.09` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 102,510.00 USD | 58,250.00 USD | 69,640.00 USD |
| `7D` | `1.09` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 71,650.00 USD | 23,780.00 USD | 85,300.00 USD |
| `7D` | `1.09` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 70,660.00 USD | 25,310.00 USD | 32,870.00 USD |
| `7D` | `1.09` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 59,760.00 USD | 39,810.00 USD | 62,330.00 USD |
| `7D` | `1.09` | 13,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 54,830.00 USD | 23,050.00 USD | 92,520.00 USD |
| `7D` | `1.10` | 13,180,000.00 USD | 13,180,000.00 USD | 0.00 USD | 92,660.00 USD | 13,440.00 USD | 38,150.00 USD |
| `7D` | `1.10` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 188,000.00 USD | 48,960.00 USD | 89,650.00 USD |
| `7D` | `1.10` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 122,300.00 USD | 43,950.00 USD | 15,590.00 USD |
| `7D` | `1.10` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 91,720.00 USD | 19,120.00 USD | 110,190.00 USD |
| `7D` | `1.10` | 13,970,000.00 USD | 13,970,000.00 USD | 0.00 USD | 22,500.00 USD | 10,330.00 USD | 31,450.00 USD |
| `7D` | `1.11` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 51,840.00 USD | 24,560.00 USD | 34,190.00 USD |
| `7D` | `1.11` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 80,930.00 USD | 42,090.00 USD | 56,110.00 USD |
| `7D` | `1.11` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 77,150.00 USD | 18,170.00 USD | 64,910.00 USD |
| `7D` | `1.11` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 28,830.00 USD | 43,670.00 USD | 25,640.00 USD |
| `7D` | `1.11` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 32,810.00 USD | 5,830.00 USD | 9,420.00 USD |
| `7D` | `1.12` | 14,720,000.00 USD | 14,720,000.00 USD | 0.00 USD | 75,790.00 USD | 45,850.00 USD | 32,030.00 USD |
| `7D` | `1.12` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 24,700.00 USD | 23,340.00 USD | 13,750.00 USD |
| `7D` | `1.12` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 49,110.00 USD | 31,670.00 USD | 23,330.00 USD |
| `7D` | `1.12` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 61,780.00 USD | 6,470.00 USD | 25,460.00 USD |
| `7D` | `1.12` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 18,300.00 USD | 10,300.00 USD | 29,890.00 USD |
| `7D` | `1.13` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 14,700.00 USD | 1,030.00 USD | 8,690.00 USD |
| `7D` | `1.13` | 15,170,000.00 USD | 15,170,000.00 USD | 0.00 USD | 46,320.00 USD | 10,950.00 USD | 45,770.00 USD |
| `7D` | `1.13` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 95,750.00 USD | 12,720.00 USD | 90,150.00 USD |
| `7D` | `1.13` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 66,770.00 USD | 3,820.00 USD | 27,360.00 USD |
| `7D` | `1.14` | 15,550,000.00 USD | 15,550,000.00 USD | 0.00 USD | 16,300.00 USD | 10,520.00 USD | 61,260.00 USD |
| `7D` | `1.14` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 4,780.00 USD | 5,350.00 USD | 6,530.00 USD |
| `7D` | `1.14` | 15,600,000.00 USD | 15,600,000.00 USD | 0.00 USD | 2,980.00 USD | 0.00 USD | 35,230.00 USD |
| `7D` | `1.14` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 36,300.00 USD | 8,930.00 USD | 6,790.00 USD |
| `7D` | `1.14` | 15,730,000.00 USD | 15,730,000.00 USD | 0.00 USD | 36,560.00 USD | 1,660.00 USD | 37,230.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `174.80M` | Total OI Tokens: `187,091,458.6 DOT`
  * 1h OI Change: `+0.08%` | 4h OI Change: `-5.52%` | 24h OI Change: `-16.49%`
  * Exchange Breakdown: Binance=`35.37M` | Bybit=`21.81M` | OKX=`10.34M` | Hyperliquid=`5.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.34K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0275%` |
| **USDT Bybit** | `0.0018%` | **USDT KuCoin** | `-0.0138%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0014%` | **USDT Bitget** | `0.0028%` |
| **CoinM Binance** | `0.0023%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `53.28%` | `46.72%` | `1.14` | 7,240,000.00 USD |
| `15M` | `Binance` | `50.64%` | `49.36%` | `1.03` | 3,040,000.00 USD |
| `15M` | `OKX` | `58.92%` | `41.08%` | `1.43` | 904,450.00 USD |
| `15M` | `Bybit` | `54.3%` | `45.7%` | `1.19` | 1,080,000.00 USD |
| `15M` | `KuCoin` | `73.22%` | `26.78%` | `2.73` | 81,810.00 USD |
| `15M` | `Gate` | `42.74%` | `57.26%` | `0.75` | 120,900.00 USD |
| `15M` | `Bitget` | `36.57%` | `63.43%` | `0.58` | 447,870.00 USD |
| `15M` | `BingX` | `61.22%` | `38.78%` | `1.58` | 346,420.00 USD |
| `15M` | `MEXC` | `48.27%` | `51.73%` | `0.93` | 454,490.00 USD |
| `15M` | `Bitunix` | `47.7%` | `52.3%` | `0.91` | 354,880.00 USD |
| `15M` | `Hyperliquid` | `67.58%` | `32.42%` | `2.08` | 174,600.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.65%` | `55.35%` | `0.81` | 26,990.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.94%` | `1.06%` | `93.34` | 155,310.00 USD |
| `15M` | `HTX` | `36.34%` | `63.66%` | `0.57` | 5,670.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `99.66%` | `0.34%` | `293.12` | 16,440.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `80.51%` | `19.49%` | `4.13` | 14,840.00 USD |
| `15M` | `Whale Positions` | `50.64%` | `49.36%` | `1.03` | 3,040,000.00 USD |
| `15M` | `Global Accounts` | `53.28%` | `46.72%` | `1.14` | 7,240,000.00 USD |
| `1H` | `DOT` | `54.18%` | `45.82%` | `1.18` | 37,400,000.00 USD |
| `1H` | `Binance` | `53.64%` | `46.36%` | `1.16` | 15,660,000.00 USD |
| `1H` | `OKX` | `58.54%` | `41.46%` | `1.41` | 5,550,000.00 USD |
| `1H` | `Bybit` | `51.98%` | `48.02%` | `1.08` | 5,510,000.00 USD |
| `1H` | `KuCoin` | `51.57%` | `48.43%` | `1.06` | 648,690.00 USD |
| `1H` | `Gate` | `45.89%` | `54.11%` | `0.85` | 820,140.00 USD |
| `1H` | `Bitget` | `39.41%` | `60.59%` | `0.65` | 1,400,000.00 USD |
| `1H` | `BingX` | `53.16%` | `46.84%` | `1.13` | 1,410,000.00 USD |
| `1H` | `MEXC` | `58.73%` | `41.27%` | `1.42` | 2,690,000.00 USD |
| `1H` | `Bitunix` | `45.29%` | `54.71%` | `0.83` | 1,610,000.00 USD |
| `1H` | `Hyperliquid` | `39.49%` | `60.51%` | `0.65` | 917,680.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `88.7%` | `11.3%` | `7.85` | 655,940.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.56%` | `0.44%` | `226.27` | 378,300.00 USD |
| `1H` | `HTX` | `49.44%` | `50.56%` | `0.98` | 32,800.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `83.32%` | `16.68%` | `5.00` | 80,550.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.51%` | `31.49%` | `2.18` | 32,580.00 USD |
| `1H` | `Whale Positions` | `53.64%` | `46.36%` | `1.16` | 15,660,000.00 USD |
| `1H` | `Global Accounts` | `54.18%` | `45.82%` | `1.18` | 37,400,000.00 USD |
| `4H` | `DOT` | `54.47%` | `45.53%` | `1.20` | 377,330,000.00 USD |
| `4H` | `Binance` | `53.35%` | `46.65%` | `1.14` | 149,930,000.00 USD |
| `4H` | `OKX` | `55.88%` | `44.12%` | `1.27` | 46,220,000.00 USD |
| `4H` | `Bybit` | `56.08%` | `43.92%` | `1.28` | 48,310,000.00 USD |
| `4H` | `KuCoin` | `53.85%` | `46.15%` | `1.17` | 2,020,000.00 USD |
| `4H` | `Gate` | `48.07%` | `51.93%` | `0.93` | 15,580,000.00 USD |
| `4H` | `Bitget` | `54.57%` | `45.43%` | `1.20` | 21,070,000.00 USD |
| `4H` | `BingX` | `57.5%` | `42.5%` | `1.35` | 16,590,000.00 USD |
| `4H` | `MEXC` | `54.49%` | `45.51%` | `1.20` | 13,860,000.00 USD |
| `4H` | `Bitunix` | `55.16%` | `44.84%` | `1.23` | 7,290,000.00 USD |
| `4H` | `Hyperliquid` | `53.15%` | `46.85%` | `1.13` | 42,590,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.82%` | `44.18%` | `1.26` | 1,720,000.00 USD |
| `4H` | `Crypto.com` | `40.94%` | `59.06%` | `0.69` | 22,840.00 USD |
| `4H` | `WhiteBIT` | `86.71%` | `13.29%` | `6.52` | 6,330,000.00 USD |
| `4H` | `HTX` | `44.44%` | `55.56%` | `0.80` | 366,550.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.46%` | `47.54%` | `1.10` | 1,350,000.00 USD |
| `4H` | `Aster` | `23.63%` | `76.37%` | `0.31` | 2,160,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.4%` | `49.6%` | `1.02` | 1,930,000.00 USD |
| `4H` | `Whale Positions` | `53.35%` | `46.65%` | `1.14` | 149,930,000.00 USD |
| `4H` | `Global Accounts` | `54.47%` | `45.53%` | `1.20` | 377,330,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9041` | `0.9059` | `0.9041` | `0.9121` | `0.9022` | 1,124,680.00 USD | 451,427.52 USD | 673,252.48 USD | -221,824.96 USD | `-19.72%` | `19B / 6S` |
| `5:00 UTC` | `0.9141` | `0.9167` | `0.9141` | `0.9231` | `0.9118` | 773,293.12 USD | 467,556.11 USD | 305,737.01 USD | 161,819.09 USD | `+20.93%` | `24B / 7S` |
| `0:00 UTC` | `0.9221` | `0.9217` | `0.9221` | `0.9232` | `0.9187` | 866,180.64 USD | 516,857.79 USD | 349,322.85 USD | 167,534.95 USD | `+19.34%` | `5B / 8S` |
| `5:00 UTC` | `0.9201` | `0.9176` | `0.9201` | `0.9222` | `0.9147` | 486,388.28 USD | 243,662.09 USD | 242,726.19 USD | 935.89 USD | `+0.19%` | `11B / 18S` |
| `0:00 UTC` | `0.9193` | `0.9207` | `0.9193` | `0.9244` | `0.9172` | 1,009,160.47 USD | 369,502.50 USD | 639,657.97 USD | -270,155.47 USD | `-26.77%` | `7B / 22S` |
| `5:00 UTC` | `0.9247` | `0.9214` | `0.9247` | `0.9264` | `0.9171` | 592,145.67 USD | 331,376.92 USD | 260,768.76 USD | 70,608.16 USD | `+11.92%` | `20B / 3S` |
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9313` | `0.9325` | `0.9332` | `0.9288` | 460,782.09 USD | 246,949.11 USD | 213,832.98 USD | 33,116.12 USD | `+7.19%` | `4B / 5S` |

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
| `5m` | 8,680.00 USD | 20,580.00 USD | **`ACCUMULATION`** |
| `15m` | -30,070.00 USD | 68,450.00 USD | **`ACCUMULATION`** |
| `30m` | -39,290.00 USD | -70,040.00 USD | **`DISTRIBUTION`** |
| `1h` | 35,720.00 USD | 262,860.00 USD | **`ACCUMULATION`** |
| `2h` | 28,870.00 USD | 567,910.00 USD | **`ACCUMULATION`** |
| `4h` | 196,610.00 USD | 3,410,000.00 USD | **`ACCUMULATION`** |
| `6h` | -183,990.00 USD | 1,180,000.00 USD | **`ACCUMULATION`** |
| `8h` | -756,710.00 USD | -4,910,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,090,000.00 USD | -5,680,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,090,000.00 USD | -6,650,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,190,000.00 USD | -23,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,770,000.00 USD | -77,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+8.68K` | 15m=`-30.07K` | 1h=`+35.72K` | 24h=`-1.09M`
* Futures Capital Netflows: 5m=`+20.58K` | 15m=`+68.45K` | 1h=`+262.86K` | 24h=`-6.65M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8932` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8515` (Risk Distance: `0.0417` pts)
  * +2.5R Take Profit: `0.9975`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9226` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9643` (Risk Distance: `0.0417` pts)
  * +2.5R Take Profit: `0.8183`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9395`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
