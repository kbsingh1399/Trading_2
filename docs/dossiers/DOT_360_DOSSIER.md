# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:22:41 IST` (`2026-10-30 04:52:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `0.9340` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9405` | Lower -3.00σ Band: `0.9275`
  * Upper +2.51σ Band: `0.9391` | Lower -2.51σ Band: `0.9289`
  * Upper +2.01σ Band: `0.9379` | Lower -2.01σ Band: `0.9301`
  * Upper +2.00σ Band: `0.9377` | Lower -2.00σ Band: `0.9303`
  * Upper +1.28σ Band: `0.9366` | Lower -1.28σ Band: `0.9314`
  * Upper +1.00σ Band: `0.9359` | Lower -1.00σ Band: `0.9321`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9340` | EMA-20=`0.9340` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9340` (Slope: `+0.0000`) | EMA-100=`0.9340`
  * Institutional Anchors: EMA-144=`0.9340` | EMA-200=`0.9340` (Slope: `+0.0000`) | EMA-233=`0.9340`
- **Range Boundaries**: 24H High=`0.9433` | 24H Low=`0.9247` | Weekly High=`0.9527` | Weekly Low=`0.9153`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9244` (Distance: `+1.03%`)
  * Point of Control (POC) = `0.9112` (Distance: `+2.50%`)
  * Value Area Low (VAL) = `0.8942` (Distance: `+4.46%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.02` | Weekly POC=`0.9945` | Weekly VAL=`0.9713`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9377` | Low=`0.9303`
  * New York Session (13:00-21:00 UTC): High=`0.9396` | Low=`0.9284`
  * Initial Balance (First Hour): IB High=`0.9368` | IB Low=`0.9312`
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
| `5m` | `0.9341` | `0.9359` | `0.9332` | `0.9351` | `148,224` | 138,552.59 USD | 8,284.90 USD | `+5.98%` | -4,000,386.00 USD | `+0.10` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.9351` | `0.9356` | `0.9339` | `0.9348` | `124,967` | 116,794.07 USD | 19,984.13 USD | `+17.11%` | -3,980,401.88 USD | `+0.25` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9347` | `0.9352` | `0.9333` | `0.9351` | `77,752` | 72,636.68 USD | 1,783.70 USD | `+2.46%` | -3,978,618.18 USD | `+0.05` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9318` | `0.9327` | `0.9263` | `0.9308` | `565,610` | 525,506.21 USD | -2,547.17 USD | `-0.48%` | -4,037,989.51 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9308` | `0.9343` | `0.9288` | `0.9342` | `533,766` | 497,143.85 USD | 29,318.60 USD | `+5.90%` | -4,008,670.91 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9341` | `0.9359` | `0.9332` | `0.9351` | `350,943` | 327,983.35 USD | 30,052.73 USD | `+9.16%` | -3,978,618.18 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.9068` | `0.9231` | `0.9022` | `0.9175` | `3,555,217` | 3,250,542.04 USD | 108,464.97 USD | `+3.34%` | -3,777,368.70 USD | `+0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9176` | `0.9341` | `0.9170` | `0.9318` | `3,070,214` | 2,839,814.60 USD | -92,909.79 USD | `-3.27%` | -3,870,278.49 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9318` | `0.9359` | `0.9263` | `0.9351` | `1,450,319` | 1,350,633.41 USD | 56,824.16 USD | `+4.21%` | -3,813,454.33 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9359` | `0.9263` | `0.9351` | `1,450,319` | 1,350,633.41 USD | 56,824.16 USD | `+4.21%` | -3,951,095.09 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -92,512.40 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -889,577.85 USD | `-1.35` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,414,306.57 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9341` | `0.8671` | `0.9318` | `27,623,369` | 24,910,302.08 USD | 1,406,387.33 USD | `+5.65%` | -4,007,919.25 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9318` | `0.9359` | `0.9263` | `0.9351` | `1,450,319` | 1,350,633.41 USD | 56,824.16 USD | `+4.21%` | -3,951,095.09 USD | `+0.39` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

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
| `7D` | `Long Liquidation` | `0.7700` | 2,880,000.00 USD | 2,880,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7720` | 2,870,000.00 USD | 2,870,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 134,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7740` | 2,860,000.00 USD | 2,860,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7760` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 130,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7780` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 128,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7800` | 2,850,000.00 USD | 2,850,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7820` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7840` | 2,840,000.00 USD | 2,840,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7860` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 128,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7880` | 2,840,000.00 USD | 2,840,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7900` | 2,830,000.00 USD | 2,830,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 127,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7920` | 2,820,000.00 USD | 2,820,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7940` | 2,790,000.00 USD | 2,790,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7960` | 2,760,000.00 USD | 2,760,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7980` | 2,740,000.00 USD | 2,740,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8000` | 2,710,000.00 USD | 2,710,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8020` | 2,690,000.00 USD | 2,690,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8040` | 2,670,000.00 USD | 2,670,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8060` | 2,660,000.00 USD | 2,660,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8080` | 2,620,000.00 USD | 2,620,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8100` | 2,610,000.00 USD | 2,610,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8120` | 2,600,000.00 USD | 2,600,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 127,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8140` | 2,570,000.00 USD | 2,570,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8160` | 2,520,000.00 USD | 2,520,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8180` | 2,460,000.00 USD | 2,460,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8200` | 2,440,000.00 USD | 2,440,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 126,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8220` | 2,430,000.00 USD | 2,430,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8230` | 2,100,000.00 USD | 2,100,000.00 USD | 2,020.00 USD | 3,730.00 USD | 912.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 124,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8240` | 2,400,000.00 USD | 2,400,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8250` | 2,090,000.00 USD | 2,090,000.00 USD | 13,200.00 USD | 5,470.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8260` | 2,360,000.00 USD | 2,360,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8270` | 2,060,000.00 USD | 2,060,000.00 USD | 3,460.00 USD | 6,970.00 USD | 110.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8280` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8290` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 1,470.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8300` | 2,340,000.00 USD | 2,340,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8310` | 2,050,000.00 USD | 2,050,000.00 USD | 295.97 USD | 1,910.00 USD | 469.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8320` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8330` | 2,040,000.00 USD | 2,040,000.00 USD | 27,680.00 USD | 1,080.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8340` | 2,330,000.00 USD | 2,330,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8350` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 4,750.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8360` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 124,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8370` | 1,990,000.00 USD | 1,990,000.00 USD | 18,030.00 USD | 2,360.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8380` | 2,280,000.00 USD | 2,280,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8390` | 1,960,000.00 USD | 1,960,000.00 USD | 671.95 USD | 745.84 USD | 1,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8400` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8410` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 449.73 USD | 933.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 123,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8420` | 2,250,000.00 USD | 2,250,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8430` | 1,960,000.00 USD | 1,960,000.00 USD | 1,590.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 751.39 USD | 122,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8440` | 2,240,000.00 USD | 2,240,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8450` | 1,950,000.00 USD | 1,950,000.00 USD | 2,200.00 USD | 6,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8460` | 2,230,000.00 USD | 2,230,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8470` | 1,950,000.00 USD | 1,950,000.00 USD | 21,360.00 USD | 407.56 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8480` | 2,220,000.00 USD | 2,220,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8490` | 1,920,000.00 USD | 1,920,000.00 USD | 198.50 USD | 142.65 USD | 537.83 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 121,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8500` | 2,190,000.00 USD | 2,190,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8510` | 1,920,000.00 USD | 1,920,000.00 USD | 6,130.00 USD | 2,240.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 120,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8520` | 2,180,000.00 USD | 2,180,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8530` | 1,910,000.00 USD | 1,910,000.00 USD | 1,230.00 USD | 2,430.00 USD | 4,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8540` | 2,170,000.00 USD | 2,170,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8550` | 1,900,000.00 USD | 1,900,000.00 USD | 17,820.00 USD | 2,470.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8560` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8570` | 1,870,000.00 USD | 1,870,000.00 USD | 739.96 USD | 445.99 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 117,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8580` | 2,160,000.00 USD | 2,160,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8590` | 1,870,000.00 USD | 1,870,000.00 USD | 5,620.00 USD | 10,610.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8595` | 180.75 USD | 116,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8600` | 2,160,000.00 USD | 2,160,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8610` | 1,850,000.00 USD | 1,850,000.00 USD | 7,980.00 USD | 855.53 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8620` | 2,150,000.00 USD | 2,150,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8630` | 1,830,000.00 USD | 1,830,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 116,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8640` | 2,110,000.00 USD | 2,110,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 116,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8650` | 1,780,000.00 USD | 1,780,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8660` | 2,110,000.00 USD | 2,110,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 116,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8670` | 1,760,000.00 USD | 1,760,000.00 USD | 11,890.00 USD | 10,090.00 USD | 1,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8680` | 2,040,000.00 USD | 2,040,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8690` | 1,730,000.00 USD | 1,730,000.00 USD | 41,960.00 USD | 3,780.00 USD | 29,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 114,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8700` | 1,880,000.00 USD | 1,880,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8710` | 1,660,000.00 USD | 1,660,000.00 USD | 42,250.00 USD | 24,870.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8715` | 92,580.00 USD | 102,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8720` | 1,780,000.00 USD | 1,780,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8730` | 1,560,000.00 USD | 1,560,000.00 USD | 54,380.00 USD | 21,510.00 USD | 25,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8740` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8750` | 1,460,000.00 USD | 1,460,000.00 USD | 38,730.00 USD | 7,100.00 USD | 19,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8760` | 1,730,000.00 USD | 1,730,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 9,560.00 USD | 9,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8770` | 1,400,000.00 USD | 1,400,000.00 USD | 10,480.00 USD | 484.10 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8780` | 1,730,000.00 USD | 1,730,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8790` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 54,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8800` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8810` | 1,330,000.00 USD | 1,330,000.00 USD | 10,360.00 USD | 5,030.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8820` | 1,630,000.00 USD | 1,630,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8830` | 1,300,000.00 USD | 1,300,000.00 USD | 612.60 USD | 5,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8840` | 1,620,000.00 USD | 1,620,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8850` | 1,300,000.00 USD | 1,300,000.00 USD | 5,380.00 USD | 36,130.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8860` | 1,600,000.00 USD | 1,600,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8870` | 1,250,000.00 USD | 1,250,000.00 USD | 67,280.00 USD | 19,040.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8880` | 1,360,000.00 USD | 1,360,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8890` | 1,130,000.00 USD | 1,130,000.00 USD | 68,360.00 USD | 40,810.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8900` | 1,190,000.00 USD | 1,190,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8910` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 38,650.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8920` | 1,000,000.00 USD | 1,000,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8930` | 954,150.00 USD | 954,150.00 USD | 56,810.00 USD | 24,610.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8940` | 903,000.00 USD | 903,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8950` | 834,810.00 USD | 834,810.00 USD | 4,110.00 USD | 15,360.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8960` | 819,210.00 USD | 819,210.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8970` | 809,670.00 USD | 809,670.00 USD | 0.00 USD | 24,270.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8980` | 693,650.00 USD | 693,650.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8990` | 769,230.00 USD | 769,230.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9000` | 675,780.00 USD | 675,780.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9010` | 753,380.00 USD | 753,380.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9020` | 653,180.00 USD | 653,180.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9030` | 733,370.00 USD | 733,370.00 USD | 0.00 USD | 15,830.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9040` | 585,540.00 USD | 585,540.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9050` | 699,760.00 USD | 699,760.00 USD | 6,880.00 USD | 5,250.00 USD | 254.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9070` | 687,370.00 USD | 687,370.00 USD | 17,190.00 USD | 1,670.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9090` | 660,930.00 USD | 660,930.00 USD | 0.00 USD | 4,890.00 USD | 176.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9110` | 655,860.00 USD | 655,860.00 USD | 22,990.00 USD | 0.00 USD | 156.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9130` | 632,710.00 USD | 632,710.00 USD | 8,180.00 USD | 5,750.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9140` | 573,260.00 USD | 573,260.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9150` | 611,540.00 USD | 611,540.00 USD | 0.00 USD | 5,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9170` | 605,680.00 USD | 605,680.00 USD | 0.00 USD | 79.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9190` | 605,600.00 USD | 605,600.00 USD | 0.00 USD | 0.00 USD | 537.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9200` | 552,030.00 USD | 552,030.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9210` | 605,070.00 USD | 605,070.00 USD | 5,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9220` | 548,050.00 USD | 548,050.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9230` | 599,360.00 USD | 599,360.00 USD | 0.00 USD | 4,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9240` | 395,570.00 USD | 395,570.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9250` | 595,190.00 USD | 595,190.00 USD | 67,310.00 USD | 42,820.00 USD | 27,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9260` | 207,730.00 USD | 207,730.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9270` | 457,320.00 USD | 457,320.00 USD | 13,430.00 USD | 778.79 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9280` | 175,430.00 USD | 175,430.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9290` | 408,320.00 USD | 408,320.00 USD | 64,620.00 USD | 13,490.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9310` | 294,440.00 USD | 294,440.00 USD | 0.00 USD | 16.72 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9320` | 149,270.00 USD | 149,270.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9330` | 294,420.00 USD | 294,420.00 USD | 6,540.00 USD | 10,870.00 USD | 145.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9340` | 111,830.00 USD | 111,830.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9350` | 276,860.00 USD | 276,860.00 USD | 143,100.00 USD | 19,970.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9360` | 99,900.00 USD | 99,900.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.9370` | 102,610.00 USD | 102,610.00 USD | 55,450.00 USD | 39,710.00 USD | 7,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.9380` | 89,890.00 USD | 89,890.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 113,100.00 USD | 113,100.00 USD | 62,110.00 USD | 29,470.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9390` | 226,200.00 USD | 226,200.00 USD | 62,110.00 USD | 29,470.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 155,410.00 USD | 155,410.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9400` | 310,810.00 USD | 310,810.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9410` | 380,530.00 USD | 380,530.00 USD | 110,670.00 USD | 21,700.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9420` | 436,330.00 USD | 436,330.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9430` | 507,380.00 USD | 507,380.00 USD | 68,020.00 USD | 27,400.00 USD | 31,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9440` | 645,190.00 USD | 645,190.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9450` | 747,300.00 USD | 747,300.00 USD | 165,230.00 USD | 40,480.00 USD | 34,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9460` | 1,030,000.00 USD | 1,030,000.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9470` | 981,890.00 USD | 981,890.00 USD | 125,730.00 USD | 35,120.00 USD | 73,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9480` | 1,320,000.00 USD | 1,320,000.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9490` | 1,170,000.00 USD | 1,170,000.00 USD | 123,000.00 USD | 17,950.00 USD | 45,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9500` | 1,710,000.00 USD | 1,710,000.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9510` | 1,250,000.00 USD | 1,250,000.00 USD | 59,610.00 USD | 13,290.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9520` | 2,030,000.00 USD | 2,030,000.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9530` | 1,350,000.00 USD | 1,350,000.00 USD | 39,160.00 USD | 12,410.00 USD | 51,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9540` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9550` | 1,410,000.00 USD | 1,410,000.00 USD | 18,340.00 USD | 22,890.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9560` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9570` | 1,420,000.00 USD | 1,420,000.00 USD | 3,780.00 USD | 5,070.00 USD | 275.27 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9580` | 2,200,000.00 USD | 2,200,000.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9590` | 1,450,000.00 USD | 1,450,000.00 USD | 6,920.00 USD | 13,740.00 USD | 9,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9600` | 2,220,000.00 USD | 2,220,000.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9610` | 1,470,000.00 USD | 1,470,000.00 USD | 8,160.00 USD | 8,480.00 USD | 8,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9620` | 2,260,000.00 USD | 2,260,000.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9630` | 1,570,000.00 USD | 1,570,000.00 USD | 69,370.00 USD | 10,170.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9640` | 2,370,000.00 USD | 2,370,000.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9650` | 1,630,000.00 USD | 1,630,000.00 USD | 2,580.00 USD | 26,060.00 USD | 40,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9660` | 2,380,000.00 USD | 2,380,000.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9670` | 1,700,000.00 USD | 1,700,000.00 USD | 37,640.00 USD | 9,780.00 USD | 22,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9680` | 2,430,000.00 USD | 2,430,000.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9690` | 1,730,000.00 USD | 1,730,000.00 USD | 12,270.00 USD | 7,500.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9695` | 14,720.00 USD | 14,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9700` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9710` | 1,760,000.00 USD | 1,760,000.00 USD | 198.50 USD | 2,290.00 USD | 33,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9720` | 2,490,000.00 USD | 2,490,000.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9730` | 1,820,000.00 USD | 1,820,000.00 USD | 40,580.00 USD | 5,320.00 USD | 14,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9740` | 2,530,000.00 USD | 2,530,000.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9745` | 214.00 USD | 14,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9750` | 1,880,000.00 USD | 1,880,000.00 USD | 25,990.00 USD | 17,610.00 USD | 15,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9760` | 2,610,000.00 USD | 2,610,000.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9770` | 1,980,000.00 USD | 1,980,000.00 USD | 77,410.00 USD | 5,960.00 USD | 8,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9780` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9790` | 2,040,000.00 USD | 2,040,000.00 USD | 29,670.00 USD | 9,580.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9800` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9810` | 2,050,000.00 USD | 2,050,000.00 USD | 6,110.00 USD | 246.39 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9820` | 2,960,000.00 USD | 2,960,000.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9830` | 2,120,000.00 USD | 2,120,000.00 USD | 15,980.00 USD | 20,550.00 USD | 29,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9840` | 3,030,000.00 USD | 3,030,000.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9850` | 2,180,000.00 USD | 2,180,000.00 USD | 39,130.00 USD | 4,550.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9860` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9870` | 2,220,000.00 USD | 2,220,000.00 USD | 12,080.00 USD | 3,590.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9880` | 3,140,000.00 USD | 3,140,000.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9890` | 2,260,000.00 USD | 2,260,000.00 USD | 24,170.00 USD | 0.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9900` | 3,160,000.00 USD | 3,160,000.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9910` | 2,340,000.00 USD | 2,340,000.00 USD | 51,650.00 USD | 1,590.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9920` | 3,190,000.00 USD | 3,190,000.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9930` | 2,380,000.00 USD | 2,380,000.00 USD | 16,270.00 USD | 14,570.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9940` | 3,230,000.00 USD | 3,230,000.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9950` | 2,400,000.00 USD | 2,400,000.00 USD | 28,670.00 USD | 0.00 USD | 329.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9960` | 3,360,000.00 USD | 3,360,000.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9970` | 2,470,000.00 USD | 2,470,000.00 USD | 46,950.00 USD | 1,840.00 USD | 13,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9980` | 3,420,000.00 USD | 3,420,000.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9990` | 2,530,000.00 USD | 2,530,000.00 USD | 33,110.00 USD | 17,910.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,470,000.00 USD | 3,470,000.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,610,000.00 USD | 2,610,000.00 USD | 54,580.00 USD | 15,590.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,570,000.00 USD | 3,570,000.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,640,000.00 USD | 2,640,000.00 USD | 10,110.00 USD | 9,260.00 USD | 6,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,640,000.00 USD | 3,640,000.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,700,000.00 USD | 2,700,000.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,700,000.00 USD | 3,700,000.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 15,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,820,000.00 USD | 2,820,000.00 USD | 47,140.00 USD | 11,590.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,870,000.00 USD | 2,870,000.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,770,000.00 USD | 3,770,000.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,910,000.00 USD | 2,910,000.00 USD | 9,660.00 USD | 28,610.00 USD | 265.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,830,000.00 USD | 3,830,000.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,920,000.00 USD | 2,920,000.00 USD | 10,040.00 USD | 3,020.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.01` | 3,860,000.00 USD | 3,860,000.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,990,000.00 USD | 2,990,000.00 USD | 18,840.00 USD | 27,060.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,910,000.00 USD | 3,910,000.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,030,000.00 USD | 3,030,000.00 USD | 2,810.00 USD | 8,390.00 USD | 26,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,110,000.00 USD | 3,110,000.00 USD | 60,720.00 USD | 4,830.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,110,000.00 USD | 4,110,000.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,170,000.00 USD | 3,170,000.00 USD | 26,430.00 USD | 11,530.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,340,000.00 USD | 4,340,000.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,280,000.00 USD | 3,280,000.00 USD | 48,740.00 USD | 23,190.00 USD | 36,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.02` | 4,560,000.00 USD | 4,560,000.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.02` | 3,370,000.00 USD | 3,370,000.00 USD | 53,060.00 USD | 13,350.00 USD | 30,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 4,740,000.00 USD | 4,740,000.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,410,000.00 USD | 3,410,000.00 USD | 19,740.00 USD | 10,270.00 USD | 8,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,060,000.00 USD | 5,060,000.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,480,000.00 USD | 3,480,000.00 USD | 22,230.00 USD | 18,890.00 USD | 25,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,250,000.00 USD | 5,250,000.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,590,000.00 USD | 3,590,000.00 USD | 75,770.00 USD | 9,640.00 USD | 31,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,360,000.00 USD | 5,360,000.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,630,000.00 USD | 3,630,000.00 USD | 17,190.00 USD | 140.33 USD | 16,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.03` | 5,590,000.00 USD | 5,590,000.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.03` | 3,660,000.00 USD | 3,660,000.00 USD | 8,030.00 USD | 17,320.00 USD | 6,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.04` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 1,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 5,900,000.00 USD | 5,900,000.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,280,000.00 USD | 6,280,000.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 15,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,980,000.00 USD | 6,980,000.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 7,250,000.00 USD | 7,250,000.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,660,000.00 USD | 7,660,000.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 15,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,050,000.00 USD | 8,050,000.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,210,000.00 USD | 8,210,000.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,540,000.00 USD | 8,540,000.00 USD | 141,110.00 USD | 49,780.00 USD | 134,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,710,000.00 USD | 8,710,000.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,060,000.00 USD | 9,060,000.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,430,000.00 USD | 9,430,000.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 9,840,000.00 USD | 9,840,000.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 10,120,000.00 USD | 10,120,000.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.06` | 10,370,000.00 USD | 10,370,000.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,550,000.00 USD | 10,550,000.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 10,900,000.00 USD | 10,900,000.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,090,000.00 USD | 11,090,000.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,320,000.00 USD | 11,320,000.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,520,000.00 USD | 11,520,000.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,670,000.00 USD | 11,670,000.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,930,000.00 USD | 11,930,000.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,170,000.00 USD | 12,170,000.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 17,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,290,000.00 USD | 12,290,000.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 12,470,000.00 USD | 12,470,000.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,710,000.00 USD | 12,710,000.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 12,940,000.00 USD | 12,940,000.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,100,000.00 USD | 13,100,000.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,220,000.00 USD | 13,220,000.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.09` | 13,380,000.00 USD | 13,380,000.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,550,000.00 USD | 13,550,000.00 USD | 66,380.00 USD | 32,080.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 13,790,000.00 USD | 13,790,000.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 14,070,000.00 USD | 14,070,000.00 USD | 182,190.00 USD | 62,380.00 USD | 40,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.10` | 14,150,000.00 USD | 14,150,000.00 USD | 59,740.00 USD | 10,900.00 USD | 2,270.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.7700` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 5,060.00 USD | 1,600.00 USD | 5,080.00 USD |
| `7D` | `0.7720` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 4,990.00 USD | 0.00 USD | 2,230.00 USD |
| `7D` | `0.7740` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 5,450.00 USD | 0.00 USD | 3,310.00 USD |
| `7D` | `0.7760` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 147.66 USD |
| `7D` | `0.7780` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 3,100.00 USD | 53.43 USD |
| `7D` | `0.7800` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 436.65 USD | 25.30 USD | 0.00 USD |
| `7D` | `0.7820` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 0.00 USD | 1,920.00 USD | 1,410.00 USD |
| `7D` | `0.7840` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 227.10 USD | 1,190.00 USD | 0.00 USD |
| `7D` | `0.7860` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 2,250.00 USD | 365.01 USD |
| `7D` | `0.7880` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 5,690.00 USD | 2,050.00 USD | 723.49 USD |
| `7D` | `0.7900` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 6,940.00 USD | 2,650.00 USD | 4,030.00 USD |
| `7D` | `0.7920` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 12,590.00 USD | 2,180.00 USD | 10,760.00 USD |
| `7D` | `0.7940` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 15,680.00 USD | 2,500.00 USD | 13,480.00 USD |
| `7D` | `0.7960` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 4,520.00 USD | 7,120.00 USD | 3,290.00 USD |
| `7D` | `0.7980` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 16,210.00 USD | 3,000.00 USD | 14,230.00 USD |
| `7D` | `0.8000` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 10,100.00 USD | 5,540.00 USD | 2,430.00 USD |
| `7D` | `0.8020` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 8,990.00 USD | 4,460.00 USD | 9,540.00 USD |
| `7D` | `0.8040` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 5,500.00 USD | 2,170.00 USD | 940.33 USD |
| `7D` | `0.8060` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 16,390.00 USD | 10,990.00 USD | 10,100.00 USD |
| `7D` | `0.8080` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,570.00 USD | 1,230.00 USD | 10,210.00 USD |
| `7D` | `0.8100` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 2,890.00 USD | 2,010.00 USD | 4,690.00 USD |
| `7D` | `0.8120` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 15,720.00 USD | 3,030.00 USD | 9,400.00 USD |
| `7D` | `0.8140` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 32,880.00 USD | 6,050.00 USD | 15,910.00 USD |
| `7D` | `0.8160` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 38,200.00 USD | 10,180.00 USD | 6,010.00 USD |
| `7D` | `0.8180` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 12,550.00 USD | 2,560.00 USD | 11,440.00 USD |
| `7D` | `0.8200` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 1,740.00 USD | 1,570.00 USD | 7,460.00 USD |
| `7D` | `0.8220` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 20,390.00 USD | 6,820.00 USD | 4,490.00 USD |
| `1D` | `0.8230` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 2,020.00 USD | 3,730.00 USD | 912.40 USD |
| `7D` | `0.8240` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 23,160.00 USD | 93.73 USD | 11,990.00 USD |
| `1D` | `0.8250` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 13,200.00 USD | 5,470.00 USD | 10,590.00 USD |
| `7D` | `0.8260` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 5,220.00 USD | 3,490.00 USD | 1,560.00 USD |
| `1D` | `0.8270` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 3,460.00 USD | 6,970.00 USD | 110.11 USD |
| `7D` | `0.8280` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 0.00 USD | 3,910.00 USD | 1,040.00 USD |
| `1D` | `0.8290` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 0.00 USD | 1,470.00 USD | 3,540.00 USD |
| `7D` | `0.8300` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 9,280.00 USD | 4,780.00 USD | 2,450.00 USD |
| `1D` | `0.8310` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 295.97 USD | 1,910.00 USD | 469.54 USD |
| `7D` | `0.8320` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 401.80 USD | 77.95 USD |
| `1D` | `0.8330` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 27,680.00 USD | 1,080.00 USD | 6,640.00 USD |
| `7D` | `0.8340` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 35,710.00 USD | 10,960.00 USD | 1,980.00 USD |
| `1D` | `0.8350` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 0.00 USD | 4,750.00 USD | 11,120.00 USD |
| `7D` | `0.8360` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 0.00 USD | 844.23 USD | 311.26 USD |
| `1D` | `0.8370` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 18,030.00 USD | 2,360.00 USD | 9,180.00 USD |
| `7D` | `0.8380` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 15,240.00 USD | 633.60 USD | 539.92 USD |
| `1D` | `0.8390` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 671.95 USD | 745.84 USD | 1,400.00 USD |
| `7D` | `0.8400` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 798.38 USD | 8,060.00 USD |
| `1D` | `0.8410` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 0.00 USD | 449.73 USD | 933.95 USD |
| `7D` | `0.8420` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 6,400.00 USD | 4,650.00 USD | 4,060.00 USD |
| `1D` | `0.8430` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 1,590.00 USD | 4,690.00 USD | 0.00 USD |
| `7D` | `0.8440` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 7,170.00 USD | 24.80 USD | 0.00 USD |
| `1D` | `0.8450` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 2,200.00 USD | 6,340.00 USD | 0.00 USD |
| `7D` | `0.8460` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 2,560.00 USD | 427.62 USD | 2,660.00 USD |
| `1D` | `0.8470` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 21,360.00 USD | 407.56 USD | 0.00 USD |
| `7D` | `0.8480` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 26,310.00 USD | 10,990.00 USD | 0.00 USD |
| `1D` | `0.8490` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 198.50 USD | 142.65 USD | 537.83 USD |
| `7D` | `0.8500` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 2,050.00 USD | 477.96 USD | 4,430.00 USD |
| `1D` | `0.8510` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 6,130.00 USD | 2,240.00 USD | 7,400.00 USD |
| `7D` | `0.8520` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 5,900.00 USD | 669.43 USD | 226.67 USD |
| `1D` | `0.8530` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 1,230.00 USD | 2,430.00 USD | 4,950.00 USD |
| `7D` | `0.8540` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 254.55 USD | 2,660.00 USD | 5,540.00 USD |
| `1D` | `0.8550` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 17,820.00 USD | 2,470.00 USD | 4,030.00 USD |
| `7D` | `0.8560` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 0.00 USD | 842.92 USD | 2,180.00 USD |
| `1D` | `0.8570` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 739.96 USD | 445.99 USD | 0.00 USD |
| `7D` | `0.8580` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 3,540.00 USD | 101.30 USD | 1,270.00 USD |
| `1D` | `0.8590` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 5,620.00 USD | 10,610.00 USD | 2,050.00 USD |
| `7D` | `0.8600` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 5,820.00 USD | 211.77 USD | 383.26 USD |
| `1D` | `0.8610` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 7,980.00 USD | 855.53 USD | 13,690.00 USD |
| `7D` | `0.8620` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 7,670.00 USD | 6,050.00 USD | 26,880.00 USD |
| `1D` | `0.8630` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 39,330.00 USD | 12,290.00 USD | 2,010.00 USD |
| `7D` | `0.8640` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 4,820.00 USD | 321.30 USD | 0.00 USD |
| `1D` | `0.8650` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 17,640.00 USD | 2,110.00 USD | 1,790.00 USD |
| `7D` | `0.8660` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 45,020.00 USD | 19,050.00 USD | 2,170.00 USD |
| `1D` | `0.8670` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 11,890.00 USD | 10,090.00 USD | 1,110.00 USD |
| `7D` | `0.8680` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 92,530.00 USD | 14,760.00 USD | 50,800.00 USD |
| `1D` | `0.8690` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 41,960.00 USD | 3,780.00 USD | 29,400.00 USD |
| `7D` | `0.8700` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 81,840.00 USD | 9,460.00 USD | 7,550.00 USD |
| `1D` | `0.8710` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 42,250.00 USD | 24,870.00 USD | 28,630.00 USD |
| `7D` | `0.8720` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 5,420.00 USD | 18,020.00 USD | 11,450.00 USD |
| `1D` | `0.8730` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 54,380.00 USD | 21,510.00 USD | 25,960.00 USD |
| `7D` | `0.8740` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 12,360.00 USD | 3,200.00 USD |
| `1D` | `0.8750` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 38,730.00 USD | 7,100.00 USD | 19,010.00 USD |
| `7D` | `0.8760` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 766.43 USD | 0.00 USD | 5,750.00 USD |
| `1D` | `0.8770` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 10,480.00 USD | 484.10 USD | 2,530.00 USD |
| `7D` | `0.8780` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 1,500.00 USD | 0.00 USD | 33,650.00 USD |
| `1D` | `0.8790` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 54,510.00 USD |
| `7D` | `0.8800` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 5,580.00 USD | 51,030.00 USD |
| `1D` | `0.8810` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 10,360.00 USD | 5,030.00 USD | 7,750.00 USD |
| `7D` | `0.8820` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 454.20 USD | 9,500.00 USD | 0.00 USD |
| `1D` | `0.8830` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 612.60 USD | 5,570.00 USD | 0.00 USD |
| `7D` | `0.8840` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 2,090.00 USD | 6,440.00 USD | 15,690.00 USD |
| `1D` | `0.8850` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 5,380.00 USD | 36,130.00 USD | 11,180.00 USD |
| `7D` | `0.8860` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 141,730.00 USD | 22,320.00 USD | 78,280.00 USD |
| `1D` | `0.8870` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 67,280.00 USD | 19,040.00 USD | 32,750.00 USD |
| `7D` | `0.8880` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 130,140.00 USD | 31,410.00 USD | 9,920.00 USD |
| `1D` | `0.8890` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 68,360.00 USD | 40,810.00 USD | 4,860.00 USD |
| `7D` | `0.8900` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 106,830.00 USD | 45,590.00 USD | 30,420.00 USD |
| `1D` | `0.8910` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 38,650.00 USD | 20,050.00 USD |
| `7D` | `0.8920` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 46,210.00 USD | 38,810.00 USD | 14,520.00 USD |
| `1D` | `0.8930` | 954,150.00 USD | 0.00 USD | 954,150.00 USD | 56,810.00 USD | 24,610.00 USD | 37,920.00 USD |
| `7D` | `0.8940` | 903,000.00 USD | 0.00 USD | 903,000.00 USD | 45,210.00 USD | 12,120.00 USD | 26,470.00 USD |
| `1D` | `0.8950` | 834,810.00 USD | 0.00 USD | 834,810.00 USD | 4,110.00 USD | 15,360.00 USD | 5,670.00 USD |
| `7D` | `0.8960` | 819,210.00 USD | 0.00 USD | 819,210.00 USD | 0.00 USD | 32,500.00 USD | 93,060.00 USD |
| `1D` | `0.8970` | 809,670.00 USD | 0.00 USD | 809,670.00 USD | 0.00 USD | 24,270.00 USD | 16,170.00 USD |
| `7D` | `0.8980` | 693,650.00 USD | 0.00 USD | 693,650.00 USD | 0.00 USD | 17,870.00 USD | 0.00 USD |
| `1D` | `0.8990` | 769,230.00 USD | 0.00 USD | 769,230.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `0.9000` | 675,780.00 USD | 0.00 USD | 675,780.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `0.9010` | 753,380.00 USD | 0.00 USD | 753,380.00 USD | 0.00 USD | 20,010.00 USD | 0.00 USD |
| `7D` | `0.9020` | 653,180.00 USD | 0.00 USD | 653,180.00 USD | 0.00 USD | 44,210.00 USD | 23,430.00 USD |
| `1D` | `0.9030` | 733,370.00 USD | 0.00 USD | 733,370.00 USD | 0.00 USD | 15,830.00 USD | 17,790.00 USD |
| `7D` | `0.9040` | 585,540.00 USD | 0.00 USD | 585,540.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD |
| `1D` | `0.9050` | 699,760.00 USD | 0.00 USD | 699,760.00 USD | 6,880.00 USD | 5,250.00 USD | 254.51 USD |
| `1D` | `0.9070` | 687,370.00 USD | 0.00 USD | 687,370.00 USD | 17,190.00 USD | 1,670.00 USD | 7,590.00 USD |
| `1D` | `0.9090` | 660,930.00 USD | 0.00 USD | 660,930.00 USD | 0.00 USD | 4,890.00 USD | 176.94 USD |
| `1D` | `0.9110` | 655,860.00 USD | 0.00 USD | 655,860.00 USD | 22,990.00 USD | 0.00 USD | 156.70 USD |
| `1D` | `0.9130` | 632,710.00 USD | 0.00 USD | 632,710.00 USD | 8,180.00 USD | 5,750.00 USD | 7,240.00 USD |
| `7D` | `0.9140` | 573,260.00 USD | 0.00 USD | 573,260.00 USD | 0.00 USD | 515.41 USD | 20,720.00 USD |
| `1D` | `0.9150` | 611,540.00 USD | 0.00 USD | 611,540.00 USD | 0.00 USD | 5,860.00 USD | 0.00 USD |
| `1D` | `0.9170` | 605,680.00 USD | 0.00 USD | 605,680.00 USD | 0.00 USD | 79.80 USD | 0.00 USD |
| `1D` | `0.9190` | 605,600.00 USD | 0.00 USD | 605,600.00 USD | 0.00 USD | 0.00 USD | 537.83 USD |
| `7D` | `0.9200` | 552,030.00 USD | 0.00 USD | 552,030.00 USD | 0.00 USD | 0.00 USD | 3,970.00 USD |
| `1D` | `0.9210` | 605,070.00 USD | 0.00 USD | 605,070.00 USD | 5,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.9220` | 548,050.00 USD | 0.00 USD | 548,050.00 USD | 152,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9230` | 599,360.00 USD | 0.00 USD | 599,360.00 USD | 0.00 USD | 4,160.00 USD | 0.00 USD |
| `7D` | `0.9240` | 395,570.00 USD | 0.00 USD | 395,570.00 USD | 145,560.00 USD | 12,790.00 USD | 29,500.00 USD |
| `1D` | `0.9250` | 595,190.00 USD | 0.00 USD | 595,190.00 USD | 67,310.00 USD | 42,820.00 USD | 27,740.00 USD |
| `7D` | `0.9260` | 207,730.00 USD | 0.00 USD | 207,730.00 USD | 0.00 USD | 32,300.00 USD | 0.00 USD |
| `1D` | `0.9270` | 457,320.00 USD | 0.00 USD | 457,320.00 USD | 13,430.00 USD | 778.79 USD | 34,800.00 USD |
| `7D` | `0.9280` | 175,430.00 USD | 0.00 USD | 175,430.00 USD | 0.00 USD | 24,550.00 USD | 1,600.00 USD |
| `1D` | `0.9290` | 408,320.00 USD | 0.00 USD | 408,320.00 USD | 64,620.00 USD | 13,490.00 USD | 35,780.00 USD |
| `1D` | `0.9310` | 294,440.00 USD | 0.00 USD | 294,440.00 USD | 0.00 USD | 16.72 USD | 0.00 USD |
| `7D` | `0.9320` | 149,270.00 USD | 0.00 USD | 149,270.00 USD | 37,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.9330` | 294,420.00 USD | 0.00 USD | 294,420.00 USD | 6,540.00 USD | 10,870.00 USD | 145.41 USD |
| `7D` | `0.9340` | 111,830.00 USD | 0.00 USD | 111,830.00 USD | 0.00 USD | 11,160.00 USD | 768.64 USD |
| `1D` | `0.9350` | 276,860.00 USD | 0.00 USD | 276,860.00 USD | 143,100.00 USD | 19,970.00 USD | 11,170.00 USD |
| `7D` | `0.9360` | 99,900.00 USD | 0.00 USD | 99,900.00 USD | 8,250.00 USD | 0.00 USD | 1,760.00 USD |
| `1D` | `0.9370` | 102,610.00 USD | 0.00 USD | 102,610.00 USD | 55,450.00 USD | 39,710.00 USD | 7,460.00 USD |
| `7D` | `0.9380` | 89,890.00 USD | 0.00 USD | 89,890.00 USD | 42,660.00 USD | 19,540.00 USD | 27,700.00 USD |
| `1D` | `0.9390` | 113,100.00 USD | 113,100.00 USD | 0.00 USD | 62,110.00 USD | 29,470.00 USD | 21,520.00 USD |
| `1D` | `0.9390` | 226,200.00 USD | 226,200.00 USD | 0.00 USD | 62,110.00 USD | 29,470.00 USD | 21,520.00 USD |
| `7D` | `0.9400` | 155,410.00 USD | 155,410.00 USD | 0.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD |
| `7D` | `0.9400` | 310,810.00 USD | 310,810.00 USD | 0.00 USD | 75,540.00 USD | 32,570.00 USD | 47,300.00 USD |
| `1D` | `0.9410` | 380,530.00 USD | 380,530.00 USD | 0.00 USD | 110,670.00 USD | 21,700.00 USD | 21,970.00 USD |
| `7D` | `0.9420` | 436,330.00 USD | 436,330.00 USD | 0.00 USD | 106,320.00 USD | 7,050.00 USD | 12,150.00 USD |
| `1D` | `0.9430` | 507,380.00 USD | 507,380.00 USD | 0.00 USD | 68,020.00 USD | 27,400.00 USD | 31,420.00 USD |
| `7D` | `0.9440` | 645,190.00 USD | 645,190.00 USD | 0.00 USD | 102,440.00 USD | 49,100.00 USD | 57,320.00 USD |
| `1D` | `0.9450` | 747,300.00 USD | 747,300.00 USD | 0.00 USD | 165,230.00 USD | 40,480.00 USD | 34,210.00 USD |
| `7D` | `0.9460` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 286,390.00 USD | 27,270.00 USD | 67,290.00 USD |
| `1D` | `0.9470` | 981,890.00 USD | 981,890.00 USD | 0.00 USD | 125,730.00 USD | 35,120.00 USD | 73,730.00 USD |
| `7D` | `0.9480` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 193,280.00 USD | 10,340.00 USD | 95,080.00 USD |
| `1D` | `0.9490` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 123,000.00 USD | 17,950.00 USD | 45,880.00 USD |
| `7D` | `0.9500` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 196,070.00 USD | 18,830.00 USD | 166,730.00 USD |
| `1D` | `0.9510` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 59,610.00 USD | 13,290.00 USD | 9,510.00 USD |
| `7D` | `0.9520` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 175,720.00 USD | 9,750.00 USD | 142,330.00 USD |
| `1D` | `0.9530` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 39,160.00 USD | 12,410.00 USD | 51,930.00 USD |
| `7D` | `0.9540` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 9,460.00 USD | 105,500.00 USD |
| `1D` | `0.9550` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 18,340.00 USD | 22,890.00 USD | 13,960.00 USD |
| `7D` | `0.9560` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 28,100.00 USD | 0.00 USD |
| `1D` | `0.9570` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 3,780.00 USD | 5,070.00 USD | 275.27 USD |
| `7D` | `0.9580` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 3,880.00 USD | 6,110.00 USD | 12,670.00 USD |
| `1D` | `0.9590` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 6,920.00 USD | 13,740.00 USD | 9,820.00 USD |
| `7D` | `0.9600` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 17,690.00 USD | 4,660.00 USD | 866.69 USD |
| `1D` | `0.9610` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 8,160.00 USD | 8,480.00 USD | 8,850.00 USD |
| `7D` | `0.9620` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 17,990.00 USD | 16,630.00 USD | 0.00 USD |
| `1D` | `0.9630` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 69,370.00 USD | 10,170.00 USD | 10,820.00 USD |
| `7D` | `0.9640` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 95,370.00 USD | 7,500.00 USD | 12,040.00 USD |
| `1D` | `0.9650` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 2,580.00 USD | 26,060.00 USD | 40,240.00 USD |
| `7D` | `0.9660` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 5,050.00 USD | 5,170.00 USD | 778.15 USD |
| `1D` | `0.9670` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 37,640.00 USD | 9,780.00 USD | 22,940.00 USD |
| `7D` | `0.9680` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 38,090.00 USD | 5,870.00 USD | 0.00 USD |
| `1D` | `0.9690` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 12,270.00 USD | 7,500.00 USD | 3,950.00 USD |
| `7D` | `0.9700` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 30,140.00 USD | 30,500.00 USD |
| `1D` | `0.9710` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 198.50 USD | 2,290.00 USD | 33,970.00 USD |
| `7D` | `0.9720` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 1,430.00 USD | 3,960.00 USD | 0.00 USD |
| `1D` | `0.9730` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 40,580.00 USD | 5,320.00 USD | 14,230.00 USD |
| `7D` | `0.9740` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 1,480.00 USD | 25,640.00 USD | 10,230.00 USD |
| `1D` | `0.9750` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 25,990.00 USD | 17,610.00 USD | 15,420.00 USD |
| `7D` | `0.9760` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 51,990.00 USD | 16,870.00 USD | 9,280.00 USD |
| `1D` | `0.9770` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 77,410.00 USD | 5,960.00 USD | 8,760.00 USD |
| `7D` | `0.9780` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,280.00 USD |
| `1D` | `0.9790` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 29,670.00 USD | 9,580.00 USD | 25,880.00 USD |
| `7D` | `0.9800` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152,470.00 USD |
| `1D` | `0.9810` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 6,110.00 USD | 246.39 USD | 6,750.00 USD |
| `7D` | `0.9820` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 53,310.00 USD | 15,990.00 USD | 104,160.00 USD |
| `1D` | `0.9830` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 15,980.00 USD | 20,550.00 USD | 29,620.00 USD |
| `7D` | `0.9840` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 49,930.00 USD | 211.77 USD | 22,300.00 USD |
| `1D` | `0.9850` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 39,130.00 USD | 4,550.00 USD | 18,830.00 USD |
| `7D` | `0.9860` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `0.9870` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 12,080.00 USD | 3,590.00 USD | 20,490.00 USD |
| `7D` | `0.9880` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 40,020.00 USD | 0.00 USD | 67,460.00 USD |
| `1D` | `0.9890` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 24,170.00 USD | 0.00 USD | 20,110.00 USD |
| `7D` | `0.9900` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 906.61 USD |
| `1D` | `0.9910` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 51,650.00 USD | 1,590.00 USD | 26,540.00 USD |
| `7D` | `0.9920` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 1,570.00 USD | 479.24 USD | 21,240.00 USD |
| `1D` | `0.9930` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 16,270.00 USD | 14,570.00 USD | 1,710.00 USD |
| `7D` | `0.9940` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 29,270.00 USD | 0.00 USD | 16,080.00 USD |
| `1D` | `0.9950` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 28,670.00 USD | 0.00 USD | 329.08 USD |
| `7D` | `0.9960` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 75,810.00 USD | 5,380.00 USD | 43,230.00 USD |
| `1D` | `0.9970` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 46,950.00 USD | 1,840.00 USD | 13,030.00 USD |
| `7D` | `0.9980` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 53,110.00 USD | 6,740.00 USD | 4,210.00 USD |
| `1D` | `0.9990` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 33,110.00 USD | 17,910.00 USD | 10,730.00 USD |
| `7D` | `1.00` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 52,850.00 USD | 0.00 USD | 462.12 USD |
| `1D` | `1.00` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 54,580.00 USD | 15,590.00 USD | 13,690.00 USD |
| `7D` | `1.00` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 54,650.00 USD | 21,850.00 USD | 16,840.00 USD |
| `1D` | `1.00` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 10,110.00 USD | 9,260.00 USD | 6,140.00 USD |
| `7D` | `1.00` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 70,950.00 USD | 3,970.00 USD | 1,470.00 USD |
| `1D` | `1.00` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 54,780.00 USD | 5,480.00 USD | 5,820.00 USD |
| `7D` | `1.01` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 46,710.00 USD | 0.00 USD | 11,560.00 USD |
| `1D` | `1.01` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 47,140.00 USD | 11,590.00 USD | 53,290.00 USD |
| `7D` | `1.01` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,430.00 USD |
| `1D` | `1.01` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 30,870.00 USD | 13,790.00 USD | 7,610.00 USD |
| `7D` | `1.01` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 10,260.00 USD | 14,180.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 9,660.00 USD | 28,610.00 USD | 265.91 USD |
| `7D` | `1.01` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 33,230.00 USD | 30,100.00 USD | 0.00 USD |
| `1D` | `1.01` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 10,040.00 USD | 3,020.00 USD | 3,900.00 USD |
| `7D` | `1.01` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 2,870.00 USD | 28,450.00 USD | 735.11 USD |
| `1D` | `1.01` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 18,840.00 USD | 27,060.00 USD | 24,680.00 USD |
| `7D` | `1.02` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 526.60 USD | 28,470.00 USD | 11,910.00 USD |
| `1D` | `1.02` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 2,810.00 USD | 8,390.00 USD | 26,620.00 USD |
| `7D` | `1.02` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 25,010.00 USD | 21,560.00 USD |
| `1D` | `1.02` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 60,720.00 USD | 4,830.00 USD | 10,660.00 USD |
| `7D` | `1.02` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 33,820.00 USD | 84,220.00 USD | 44,250.00 USD |
| `1D` | `1.02` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 26,430.00 USD | 11,530.00 USD | 21,110.00 USD |
| `7D` | `1.02` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 56,930.00 USD | 52,610.00 USD | 112,030.00 USD |
| `1D` | `1.02` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 48,740.00 USD | 23,190.00 USD | 36,520.00 USD |
| `7D` | `1.02` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 78,220.00 USD | 56,700.00 USD | 86,740.00 USD |
| `1D` | `1.02` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 53,060.00 USD | 13,350.00 USD | 30,580.00 USD |
| `7D` | `1.03` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 22,650.00 USD | 124,880.00 USD | 33,130.00 USD |
| `1D` | `1.03` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 19,740.00 USD | 10,270.00 USD | 8,300.00 USD |
| `7D` | `1.03` | 5,060,000.00 USD | 5,060,000.00 USD | 0.00 USD | 250,310.00 USD | 50,530.00 USD | 24,480.00 USD |
| `1D` | `1.03` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 22,230.00 USD | 18,890.00 USD | 25,030.00 USD |
| `7D` | `1.03` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 134,200.00 USD | 33,660.00 USD | 19,120.00 USD |
| `1D` | `1.03` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 75,770.00 USD | 9,640.00 USD | 31,790.00 USD |
| `7D` | `1.03` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 88,380.00 USD | 213.80 USD | 19,220.00 USD |
| `1D` | `1.03` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 17,190.00 USD | 140.33 USD | 16,160.00 USD |
| `7D` | `1.03` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 217,210.00 USD | 8,290.00 USD | 4,310.00 USD |
| `1D` | `1.03` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 8,030.00 USD | 17,320.00 USD | 6,850.00 USD |
| `1D` | `1.04` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 1,430.00 USD | 0.00 USD |
| `7D` | `1.04` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 262,550.00 USD | 3,170.00 USD | 42,930.00 USD |
| `7D` | `1.04` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 178,400.00 USD | 1,290.00 USD | 199,090.00 USD |
| `7D` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 279,840.00 USD | 9,430.00 USD | 93,080.00 USD |
| `7D` | `1.04` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 167,900.00 USD | 2,070.00 USD | 154,190.00 USD |
| `7D` | `1.04` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 145,680.00 USD | 39,130.00 USD | 78,780.00 USD |
| `7D` | `1.05` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 146,550.00 USD | 90,720.00 USD | 176,980.00 USD |
| `7D` | `1.05` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 199,320.00 USD | 28,070.00 USD | 161,420.00 USD |
| `7D` | `1.05` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 91,750.00 USD | 29,070.00 USD | 40,740.00 USD |
| `7D` | `1.05` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 141,110.00 USD | 49,780.00 USD | 134,080.00 USD |
| `7D` | `1.05` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 88,940.00 USD | 44,290.00 USD | 36,750.00 USD |
| `7D` | `1.06` | 9,060,000.00 USD | 9,060,000.00 USD | 0.00 USD | 187,610.00 USD | 48,000.00 USD | 121,890.00 USD |
| `7D` | `1.06` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 205,690.00 USD | 63,350.00 USD | 94,840.00 USD |
| `7D` | `1.06` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 217,790.00 USD | 73,000.00 USD | 125,100.00 USD |
| `7D` | `1.06` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 131,720.00 USD | 83,000.00 USD | 66,000.00 USD |
| `7D` | `1.06` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 102,750.00 USD | 49,310.00 USD | 92,130.00 USD |
| `7D` | `1.07` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 77,920.00 USD | 32,860.00 USD | 73,060.00 USD |
| `7D` | `1.07` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 221,410.00 USD | 30,180.00 USD | 93,450.00 USD |
| `7D` | `1.07` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 121,300.00 USD | 33,170.00 USD | 42,800.00 USD |
| `7D` | `1.07` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 103,500.00 USD | 37,730.00 USD | 83,520.00 USD |
| `7D` | `1.07` | 11,520,000.00 USD | 11,520,000.00 USD | 0.00 USD | 92,440.00 USD | 21,500.00 USD | 83,440.00 USD |
| `7D` | `1.08` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 103,110.00 USD | 18,720.00 USD | 27,400.00 USD |
| `7D` | `1.08` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 158,650.00 USD | 40,740.00 USD | 69,670.00 USD |
| `7D` | `1.08` | 12,170,000.00 USD | 12,170,000.00 USD | 0.00 USD | 176,790.00 USD | 26,190.00 USD | 33,510.00 USD |
| `7D` | `1.08` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 62,710.00 USD | 20,510.00 USD | 39,030.00 USD |
| `7D` | `1.08` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 46,000.00 USD | 31,940.00 USD | 103,610.00 USD |
| `7D` | `1.09` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 161,270.00 USD | 28,200.00 USD | 42,090.00 USD |
| `7D` | `1.09` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 59,850.00 USD | 57,700.00 USD | 117,570.00 USD |
| `7D` | `1.09` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 109,670.00 USD | 18,350.00 USD | 31,220.00 USD |
| `7D` | `1.09` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 37,360.00 USD | 24,570.00 USD | 62,450.00 USD |
| `7D` | `1.09` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 67,090.00 USD | 37,290.00 USD | 55,440.00 USD |
| `7D` | `1.10` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 66,380.00 USD | 32,080.00 USD | 65,790.00 USD |
| `7D` | `1.10` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 119,850.00 USD | 21,050.00 USD | 97,790.00 USD |
| `7D` | `1.10` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 182,190.00 USD | 62,380.00 USD | 40,340.00 USD |
| `7D` | `1.10` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 59,740.00 USD | 10,900.00 USD | 2,270.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `175.25M` | Total OI Tokens: `186,914,217.0 DOT`
  * 1h OI Change: `+0.04%` | 4h OI Change: `-6.40%` | 24h OI Change: `-16.44%`
  * Exchange Breakdown: Binance=`35.41M` | Bybit=`21.87M` | OKX=`10.33M` | Hyperliquid=`5.84M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `737.85` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0269%` |
| **USDT Bybit** | `-0.0017%` | **USDT KuCoin** | `-0.0158%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0000%` | **USDT Bitget** | `0.0039%` |
| **CoinM Binance** | `0.0028%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `46.76%` | `53.24%` | `0.88` | 7,660,000.00 USD |
| `15M` | `Binance` | `46.55%` | `53.45%` | `0.87` | 3,070,000.00 USD |
| `15M` | `OKX` | `58.26%` | `41.74%` | `1.40` | 1,500,000.00 USD |
| `15M` | `Bybit` | `39.02%` | `60.98%` | `0.64` | 1,050,000.00 USD |
| `15M` | `KuCoin` | `48.33%` | `51.67%` | `0.94` | 44,920.00 USD |
| `15M` | `Gate` | `43.55%` | `56.45%` | `0.77` | 163,180.00 USD |
| `15M` | `Bitget` | `55.41%` | `44.59%` | `1.24` | 414,360.00 USD |
| `15M` | `BingX` | `24.71%` | `75.29%` | `0.33` | 569,410.00 USD |
| `15M` | `MEXC` | `44.37%` | `55.63%` | `0.80` | 349,300.00 USD |
| `15M` | `Bitunix` | `32.83%` | `67.17%` | `0.49` | 284,780.00 USD |
| `15M` | `Hyperliquid` | `49.16%` | `50.84%` | `0.97` | 61,830.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.89%` | `47.11%` | `1.12` | 24,880.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 100,620.00 USD |
| `15M` | `HTX` | `77.67%` | `22.33%` | `3.48` | 15,030.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `8.32%` | `91.68%` | `0.09` | 12,340.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.92%` | `55.08%` | `0.82` | 4,250.00 USD |
| `15M` | `Whale Positions` | `46.55%` | `53.45%` | `0.87` | 3,070,000.00 USD |
| `15M` | `Global Accounts` | `46.76%` | `53.24%` | `0.88` | 7,660,000.00 USD |
| `1H` | `DOT` | `48.01%` | `51.99%` | `0.92` | 30,880,000.00 USD |
| `1H` | `Binance` | `51.85%` | `48.15%` | `1.08` | 11,640,000.00 USD |
| `1H` | `OKX` | `44.07%` | `55.93%` | `0.79` | 5,470,000.00 USD |
| `1H` | `Bybit` | `44.99%` | `55.01%` | `0.82` | 2,420,000.00 USD |
| `1H` | `KuCoin` | `52.64%` | `47.36%` | `1.11` | 214,550.00 USD |
| `1H` | `Gate` | `38.68%` | `61.32%` | `0.63` | 527,350.00 USD |
| `1H` | `Bitget` | `46.28%` | `53.72%` | `0.86` | 1,300,000.00 USD |
| `1H` | `BingX` | `44.81%` | `55.19%` | `0.81` | 1,290,000.00 USD |
| `1H` | `MEXC` | `52.21%` | `47.79%` | `1.09` | 5,470,000.00 USD |
| `1H` | `Bitunix` | `54.77%` | `45.23%` | `1.21` | 948,380.00 USD |
| `1H` | `Hyperliquid` | `31.18%` | `68.82%` | `0.45` | 702,640.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.24%` | `51.76%` | `0.93` | 478,530.00 USD |
| `1H` | `Crypto.com` | `78.4%` | `21.6%` | `3.63` | 0.00 USD |
| `1H` | `WhiteBIT` | `34.72%` | `65.28%` | `0.53` | 100,080.00 USD |
| `1H` | `HTX` | `50.03%` | `49.97%` | `1.00` | 14,240.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `89.68%` | `10.32%` | `8.69` | 292,450.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `43.41%` | `56.59%` | `0.77` | 15,980.00 USD |
| `1H` | `Whale Positions` | `51.85%` | `48.15%` | `1.08` | 11,640,000.00 USD |
| `1H` | `Global Accounts` | `48.01%` | `51.99%` | `0.92` | 30,880,000.00 USD |
| `4H` | `DOT` | `52.19%` | `47.81%` | `1.09` | 141,380,000.00 USD |
| `4H` | `Binance` | `52.91%` | `47.09%` | `1.12` | 56,870,000.00 USD |
| `4H` | `OKX` | `54.85%` | `45.15%` | `1.21` | 19,210,000.00 USD |
| `4H` | `Bybit` | `52.68%` | `47.32%` | `1.11` | 18,320,000.00 USD |
| `4H` | `KuCoin` | `52.71%` | `47.29%` | `1.11` | 1,670,000.00 USD |
| `4H` | `Gate` | `53.21%` | `46.79%` | `1.14` | 4,340,000.00 USD |
| `4H` | `Bitget` | `48.53%` | `51.47%` | `0.94` | 6,770,000.00 USD |
| `4H` | `BingX` | `31.12%` | `68.88%` | `0.45` | 7,130,000.00 USD |
| `4H` | `MEXC` | `55.67%` | `44.33%` | `1.26` | 13,200,000.00 USD |
| `4H` | `Bitunix` | `46.9%` | `53.1%` | `0.88` | 4,720,000.00 USD |
| `4H` | `Hyperliquid` | `37.1%` | `62.9%` | `0.59` | 4,590,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `65.56%` | `34.44%` | `1.90` | 1,440,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `98.4%` | `1.6%` | `61.50` | 2,050,000.00 USD |
| `4H` | `HTX` | `49.54%` | `50.46%` | `0.98` | 228,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.4%` | `54.6%` | `0.83` | 364,960.00 USD |
| `4H` | `Aster` | `66.44%` | `33.56%` | `1.98` | 377,420.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.81%` | `40.19%` | `1.49` | 110,640.00 USD |
| `4H` | `Whale Positions` | `52.91%` | `47.09%` | `1.12` | 56,870,000.00 USD |
| `4H` | `Global Accounts` | `52.19%` | `47.81%` | `1.09` | 141,380,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9221` | `0.9217` | `0.9221` | `0.9232` | `0.9187` | 866,180.64 USD | 516,857.79 USD | 349,322.85 USD | 167,534.95 USD | `+19.34%` | `5B / 8S` |
| `5:00 UTC` | `0.9201` | `0.9176` | `0.9201` | `0.9222` | `0.9147` | 486,388.28 USD | 243,662.09 USD | 242,726.19 USD | 935.89 USD | `+0.19%` | `11B / 18S` |
| `0:00 UTC` | `0.9193` | `0.9207` | `0.9193` | `0.9244` | `0.9172` | 1,009,160.47 USD | 369,502.50 USD | 639,657.97 USD | -270,155.47 USD | `-26.77%` | `7B / 22S` |
| `5:00 UTC` | `0.9247` | `0.9214` | `0.9247` | `0.9264` | `0.9171` | 592,145.67 USD | 331,376.92 USD | 260,768.76 USD | 70,608.16 USD | `+11.92%` | `20B / 3S` |
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9317` | `0.9322` | `0.9342` | `0.9301` | 515,769.04 USD | 235,727.30 USD | 280,041.74 USD | -44,314.44 USD | `-8.59%` | `11B / 7S` |
| `0:00 UTC` | `0.9301` | `0.9291` | `0.9301` | `0.9327` | `0.9264` | 525,506.21 USD | 261,479.52 USD | 264,026.69 USD | -2,547.17 USD | `-0.48%` | `9B / 12S` |
| `5:00 UTC` | `0.9325` | `0.9314` | `0.9325` | `0.9344` | `0.9288` | 497,143.85 USD | 263,231.22 USD | 233,912.62 USD | 29,318.60 USD | `+5.90%` | `7B / 6S` |
| `0:00 UTC` | `0.9354` | `0.9348` | `0.9354` | `0.9365` | `0.9333` | 404,247.05 USD | 223,080.64 USD | 181,166.41 USD | 41,914.22 USD | `+10.37%` | `5B / 3S` |
| `5:00 UTC` | `0.9406` | `0.9398` | `0.9406` | `0.9425` | `0.9362` | 584,145.10 USD | 287,023.23 USD | 297,121.87 USD | -10,098.64 USD | `-1.73%` | `17B / 12S` |

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
| `5m` | -9,940.00 USD | -8,810.00 USD | **`DISTRIBUTION`** |
| `15m` | -16,510.00 USD | 48,970.00 USD | **`ACCUMULATION`** |
| `30m` | -41,090.00 USD | 117,700.00 USD | **`ACCUMULATION`** |
| `1h` | 7,960.00 USD | -12,940.00 USD | **`DISTRIBUTION`** |
| `2h` | -19,940.00 USD | 311,400.00 USD | **`ACCUMULATION`** |
| `4h` | 132,920.00 USD | 3,680,000.00 USD | **`ACCUMULATION`** |
| `6h` | -304,240.00 USD | 1,240,000.00 USD | **`ACCUMULATION`** |
| `8h` | -422,090.00 USD | -4,870,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,100,000.00 USD | -5,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,170,000.00 USD | -6,600,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,190,000.00 USD | -22,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,840,000.00 USD | -77,140,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-9.94K` | 15m=`-16.51K` | 1h=`+7.96K` | 24h=`-1.17M`
* Futures Capital Netflows: 5m=`-8.81K` | 15m=`+48.97K` | 1h=`-12.94K` | 24h=`-6.60M`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8942` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.3358` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `3.97`
  * Mathematical Lot Sizing: **`8.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9244` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.15` (Risk Distance: `1.23` pts)
  * +2.5R Take Profit: `-2.15`
  * Mathematical Lot Sizing: **`8.13 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9415`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
