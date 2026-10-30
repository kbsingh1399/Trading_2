# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:22:11 IST` (`2026-10-30 03:52:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `0.8912` | VWAP Z-Score: `+2.19` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0109` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `54.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9306` | Lower -3.00σ Band: `0.8518`
  * Upper +2.51σ Band: `0.9242` | Lower -2.51σ Band: `0.8582`
  * Upper +2.01σ Band: `0.9176` | Lower -2.01σ Band: `0.8648`
  * Upper +2.00σ Band: `0.9175` | Lower -2.00σ Band: `0.8649`
  * Upper +1.28σ Band: `0.9080` | Lower -1.28σ Band: `0.8744`
  * Upper +1.00σ Band: `0.9043` | Lower -1.00σ Band: `0.8780`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.9081` | EMA-20=`0.9086` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9278` (Slope: `+0.0000`) | EMA-100=`0.9474`
  * Institutional Anchors: EMA-144=`0.9563` | EMA-200=`0.9628` (Slope: `-0.7804`) | EMA-233=`0.9669`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9216` (Distance: `+1.18%`)
  * Point of Control (POC) = `0.9112` (Distance: `+2.34%`)
  * Value Area Low (VAL) = `0.8923` (Distance: `+4.51%`)
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
| `5m` | `0.9305` | `0.9319` | `0.9293` | `0.9314` | `299,009` | 278,213.93 USD | 123,119.49 USD | `+44.25%` | -3,839,018.70 USD | `+1.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.9313` | `0.9336` | `0.9309` | `0.9332` | `216,551` | 201,833.11 USD | -7,068.92 USD | `-3.50%` | -3,846,087.62 USD | `-0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.9332` | `0.9333` | `0.9332` | `0.9333` | `1,436` | 1,339.75 USD | 1,339.75 USD | `+100.00%` | -3,844,747.87 USD | `-0.14` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9175` | `0.9264` | `0.9170` | `0.9258` | `642,731` | 592,145.67 USD | 70,608.16 USD | `+11.92%` | -4,101,354.84 USD | `+0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.9259` | `0.9319` | `0.9246` | `0.9314` | `777,692` | 722,739.41 USD | 150,951.95 USD | `+20.89%` | -3,950,402.88 USD | `+0.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9313` | `0.9336` | `0.9309` | `0.9333` | `217,987` | 203,173.32 USD | -5,729.64 USD | `-2.82%` | -3,956,132.52 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.8988` | `0.9187` | `0.8939` | `0.9068` | `9,068,149` | 8,222,593.96 USD | 2,325,203.98 USD | `+28.28%` | -4,010,272.50 USD | `+2.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.9068` | `0.9231` | `0.9022` | `0.9175` | `3,555,217` | 3,250,542.04 USD | 108,464.97 USD | `+3.34%` | -3,901,807.53 USD | `+0.30` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.9176` | `0.9336` | `0.9170` | `0.9333` | `2,734,574` | 2,527,218.88 USD | -54,324.99 USD | `-2.15%` | -3,956,132.52 USD | `+0.15` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -876,375.92 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,401,104.65 USD | `-1.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9336` | `0.8671` | `0.9333` | `27,287,730` | 24,597,706.36 USD | 1,444,972.13 USD | `+5.87%` | -3,956,132.52 USD | `+1.13` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 98,266.33 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -79,310.47 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -876,375.92 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,401,104.65 USD | `-1.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9336` | `0.8671` | `0.9333` | `27,287,730` | 24,597,706.36 USD | 1,444,972.13 USD | `+5.87%` | -3,956,132.52 USD | `+1.13` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.02` | 5,545.81 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 5.55K USD at 1.0190 USD [API] | `2026-10-28 22:45:22` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 6,059.91 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 6.06K USD at 1.0189 USD [API] | `2026-10-28 22:45:22` |
| `ANNOUNCEMENT` | `INFO` | `1.00` | 5,995.92 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 6.00K USD at 1.0033 USD [API] | `2026-10-29 01:20:22` |
| `ANNOUNCEMENT` | `INFO` | `1.00` | 5,995.91 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale SELL: 6.00K USD at 1.0035 USD [API] | `2026-10-29 01:20:22` |


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
| `Live` | `Long Liquidation` | `0.2215` | 110.75 USD | 343,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 2,180.00 USD | 343,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 566.97 USD | 341,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3355` | 273.67 USD | 340,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3695` | 816.23 USD | 340,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4195` | 2,800.00 USD | 339,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 315.16 USD | 336,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4655` | 2,650.00 USD | 336,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4705` | 2,590.00 USD | 333,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 331,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5535` | 553.50 USD | 327,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 327,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 312,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 312,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 311,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6035` | 158.18 USD | 311,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 1,480.00 USD | 311,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 309,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 307,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 307,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6175` | 244.84 USD | 307,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 307,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 306,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6365` | 507.86 USD | 306,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 306,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 304,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 283,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 279,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 413.70 USD | 279,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 278,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 215,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 214,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 214,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 213,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7035` | 87,940.00 USD | 212,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7065` | 20,390.00 USD | 124,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 104,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 103,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 101,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 101,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 101,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 98,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 97,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 97,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 96,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7545` | 53,570.00 USD | 95,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 8,990.00 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7635` | 308.00 USD | 33,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 32,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7775` | 2,490.00 USD | 28,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 26,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 26,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,090,000.00 USD | 2,090,000.00 USD | 7,140.00 USD | 2,140.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 25,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 25,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,840,000.00 USD | 1,840,000.00 USD | 5,990.00 USD | 7,610.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,820,000.00 USD | 1,820,000.00 USD | 10,780.00 USD | 2,370.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,800,000.00 USD | 1,800,000.00 USD | 8,920.00 USD | 2,530.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,780,000.00 USD | 1,780,000.00 USD | 7,510.00 USD | 3,060.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 24,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,760,000.00 USD | 1,760,000.00 USD | 29,430.00 USD | 4,660.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 22,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 22,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,640,000.00 USD | 1,640,000.00 USD | 15,240.00 USD | 154.74 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 1,370,000.00 USD | 1,370,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 1,360,000.00 USD | 1,360,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,620,000.00 USD | 1,620,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 21,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,610,000.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,620.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 895.29 USD | 20,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 1,360,000.00 USD | 1,360,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,600,000.00 USD | 1,600,000.00 USD | 7,900.00 USD | 1,130.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,590,000.00 USD | 1,590,000.00 USD | 731.45 USD | 132.08 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 19,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 1,350,000.00 USD | 1,350,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,590,000.00 USD | 1,590,000.00 USD | 5,480.00 USD | 114.10 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 18,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,580,000.00 USD | 1,580,000.00 USD | 2,130.00 USD | 2,670.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8535` | 179.49 USD | 15,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8540` | 1,350,000.00 USD | 1,350,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,570,000.00 USD | 1,570,000.00 USD | 254.55 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,350,000.00 USD | 1,350,000.00 USD | 2,270.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 15,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 1,340,000.00 USD | 1,340,000.00 USD | 617.52 USD | 197.60 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 211.77 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 1,340,000.00 USD | 1,340,000.00 USD | 6,520.00 USD | 1,220.00 USD | 251.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,560,000.00 USD | 1,560,000.00 USD | 7,320.00 USD | 2,920.00 USD | 467.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 1,340,000.00 USD | 1,340,000.00 USD | 7,410.00 USD | 70.98 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,550,000.00 USD | 1,550,000.00 USD | 758.91 USD | 2,820.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 14,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,330,000.00 USD | 1,330,000.00 USD | 6,350.00 USD | 2,070.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 14,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,550,000.00 USD | 1,550,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 13,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,540,000.00 USD | 1,540,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,320,000.00 USD | 1,320,000.00 USD | 3,580.00 USD | 3,640.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,520,000.00 USD | 1,520,000.00 USD | 25,250.00 USD | 2,030.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 12,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,300,000.00 USD | 1,300,000.00 USD | 21,490.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,480,000.00 USD | 1,480,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,270,000.00 USD | 1,270,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,080.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,230,000.00 USD | 1,230,000.00 USD | 7,270.00 USD | 3,350.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 583.80 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,220,000.00 USD | 1,220,000.00 USD | 17,510.00 USD | 3,760.00 USD | 4,390.00 USD | `Tier 1 CEX` |
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
| `1D` | `Short Liquidation` | `0.9700` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,680,000.00 USD | 1,680,000.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,180,000.00 USD | 2,180,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9735` | 213.78 USD | 213.78 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,730,000.00 USD | 1,730,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,810,000.00 USD | 1,810,000.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,300,000.00 USD | 2,300,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,870,000.00 USD | 1,870,000.00 USD | 39,980.00 USD | 3,080.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9795` | 8,850.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,930,000.00 USD | 1,930,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,510,000.00 USD | 2,510,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9815` | 216.72 USD | 9,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.9985` | 220.47 USD | 9,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9990` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 104.05 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 220.91 USD | 9,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,050,000.00 USD | 3,050,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,200,000.00 USD | 3,200,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,440,000.00 USD | 2,440,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,230,000.00 USD | 3,230,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 9,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 10,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,030,000.00 USD | 6,030,000.00 USD | 239,580.00 USD | 8,210.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,930,000.00 USD | 6,930,000.00 USD | 184,670.00 USD | 23,680.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,450,000.00 USD | 7,450,000.00 USD | 178,890.00 USD | 96,750.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 10,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,650,000.00 USD | 7,650,000.00 USD | 116,670.00 USD | 13,190.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,960,000.00 USD | 7,960,000.00 USD | 175,350.00 USD | 43,000.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 8,160,000.00 USD | 8,160,000.00 USD | 68,590.00 USD | 58,720.00 USD | 74,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 298.35 USD | 10,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 13,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.11` | 170.02 USD | 13,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 15,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 37,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 49,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 49,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 53,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 53,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 55,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 125.25 USD | 55,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 798.29 USD | 55,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 58,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 66,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 66,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 244.39 USD | 67,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 328.44 USD | 67,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 67,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 23,630.00 USD | 91,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2215` | 343,550.00 USD | 0.00 USD | 110.75 USD | `-75.86%` | `500.00` |
| `Live` | `Long` | `0.2375` | 343,440.00 USD | 0.00 USD | 2,180.00 USD | `-74.12%` | `9,174.90` |
| `Live` | `Long` | `0.3305` | 341,260.00 USD | 0.00 USD | 566.97 USD | `-63.99%` | `1,715.50` |
| `Live` | `Long` | `0.3355` | 340,700.00 USD | 0.00 USD | 273.67 USD | `-63.44%` | `815.70` |
| `Live` | `Long` | `0.3695` | 340,420.00 USD | 0.00 USD | 816.23 USD | `-59.74%` | `2,209.00` |
| `Live` | `Long` | `0.4195` | 339,610.00 USD | 0.00 USD | 2,800.00 USD | `-54.29%` | `6,675.20` |
| `Live` | `Long` | `0.4645` | 336,810.00 USD | 0.00 USD | 315.16 USD | `-49.38%` | `678.50` |
| `Live` | `Long` | `0.4655` | 336,490.00 USD | 0.00 USD | 2,650.00 USD | `-49.28%` | `5,698.80` |
| `Live` | `Long` | `0.4705` | 333,840.00 USD | 0.00 USD | 2,590.00 USD | `-48.73%` | `5,500.00` |
| `Live` | `Long` | `0.5065` | 331,250.00 USD | 0.00 USD | 3,290.00 USD | `-44.81%` | `6,504.70` |
| `Live` | `Long` | `0.5535` | 327,960.00 USD | 0.00 USD | 553.50 USD | `-39.69%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 327,400.00 USD | 0.00 USD | 14,600.00 USD | `-38.38%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 312,800.00 USD | 0.00 USD | 577.36 USD | `-37.94%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 312,230.00 USD | 0.00 USD | 683.51 USD | `-36.31%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 311,540.00 USD | 0.00 USD | 137.53 USD | `-35.76%` | `233.30` |
| `Live` | `Long` | `0.6035` | 311,400.00 USD | 0.00 USD | 158.18 USD | `-34.24%` | `262.10` |
| `Live` | `Long` | `0.6055` | 311,250.00 USD | 0.00 USD | 1,480.00 USD | `-34.02%` | `2,448.50` |
| `Live` | `Long` | `0.6065` | 309,760.00 USD | 0.00 USD | 1,800.00 USD | `-33.91%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 307,960.00 USD | 0.00 USD | 105.96 USD | `-33.26%` | `173.00` |
| `Live` | `Long` | `0.6145` | 307,860.00 USD | 0.00 USD | 147.48 USD | `-33.04%` | `240.00` |
| `Live` | `Long` | `0.6175` | 307,710.00 USD | 0.00 USD | 244.84 USD | `-32.71%` | `396.50` |
| `Live` | `Long` | `0.6315` | 307,460.00 USD | 0.00 USD | 757.80 USD | `-31.19%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 306,710.00 USD | 0.00 USD | 106.00 USD | `-30.75%` | `166.80` |
| `Live` | `Long` | `0.6365` | 306,600.00 USD | 0.00 USD | 507.86 USD | `-30.64%` | `797.90` |
| `Live` | `Long` | `0.6405` | 306,090.00 USD | 0.00 USD | 2,090.00 USD | `-30.21%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 304,000.00 USD | 0.00 USD | 20,270.00 USD | `-30.10%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 283,730.00 USD | 0.00 USD | 4,230.00 USD | `-29.55%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 279,510.00 USD | 0.00 USD | 202.47 USD | `-29.44%` | `312.70` |
| `Live` | `Long` | `0.6595` | 279,300.00 USD | 0.00 USD | 413.70 USD | `-28.14%` | `627.30` |
| `Live` | `Long` | `0.6725` | 278,890.00 USD | 0.00 USD | 63,890.00 USD | `-26.72%` | `95,000.00` |
| `Live` | `Long` | `0.6775` | 215,000.00 USD | 0.00 USD | 423.10 USD | `-26.17%` | `624.50` |
| `Live` | `Long` | `0.6835` | 214,580.00 USD | 0.00 USD | 512.97 USD | `-25.52%` | `750.50` |
| `Live` | `Long` | `0.6965` | 214,070.00 USD | 0.00 USD | 322.62 USD | `-24.10%` | `463.20` |
| `Live` | `Long` | `0.7005` | 213,740.00 USD | 0.00 USD | 1,140.00 USD | `-23.67%` | `1,634.20` |
| `Live` | `Long` | `0.7035` | 212,600.00 USD | 0.00 USD | 87,940.00 USD | `-23.34%` | `125,000.00` |
| `Live` | `Long` | `0.7065` | 124,660.00 USD | 0.00 USD | 20,390.00 USD | `-23.01%` | `28,858.40` |
| `Live` | `Long` | `0.7145` | 104,270.00 USD | 0.00 USD | 988.87 USD | `-22.14%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 103,280.00 USD | 0.00 USD | 1,580.00 USD | `-21.38%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 101,700.00 USD | 0.00 USD | 397.93 USD | `-21.16%` | `550.00` |
| `Live` | `Long` | `0.7285` | 101,310.00 USD | 0.00 USD | 291.18 USD | `-20.62%` | `399.70` |
| `Live` | `Long` | `0.7305` | 101,010.00 USD | 0.00 USD | 2,300.00 USD | `-20.40%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 98,720.00 USD | 0.00 USD | 1,140.00 USD | `-20.07%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 97,580.00 USD | 0.00 USD | 283.30 USD | `-19.42%` | `383.10` |
| `Live` | `Long` | `0.7525` | 97,290.00 USD | 0.00 USD | 331.18 USD | `-18.00%` | `440.10` |
| `Live` | `Long` | `0.7535` | 96,960.00 USD | 0.00 USD | 1,400.00 USD | `-17.89%` | `1,859.90` |
| `Live` | `Long` | `0.7545` | 95,560.00 USD | 0.00 USD | 53,570.00 USD | `-17.78%` | `71,003.30` |
| `Live` | `Long` | `0.7555` | 41,990.00 USD | 0.00 USD | 8,990.00 USD | `-17.67%` | `11,902.80` |
| `Live` | `Long` | `0.7635` | 33,000.00 USD | 0.00 USD | 308.00 USD | `-16.80%` | `403.40` |
| `Live` | `Long` | `0.7725` | 32,690.00 USD | 0.00 USD | 3,840.00 USD | `-15.82%` | `4,968.90` |
| `Live` | `Long` | `0.7775` | 28,850.00 USD | 0.00 USD | 2,490.00 USD | `-15.28%` | `3,199.30` |
| `Live` | `Long` | `0.7795` | 26,360.00 USD | 0.00 USD | 272.83 USD | `-15.06%` | `350.00` |
| `Live` | `Long` | `0.7865` | 26,090.00 USD | 0.00 USD | 292.03 USD | `-14.30%` | `371.30` |
| `Live` | `Long` | `0.7905` | 25,800.00 USD | 0.00 USD | 277.39 USD | `-13.86%` | `350.90` |
| `Live` | `Long` | `0.8135` | 25,520.00 USD | 0.00 USD | 647.79 USD | `-11.35%` | `796.30` |
| `Live` | `Long` | `0.8215` | 24,870.00 USD | 0.00 USD | 1,950.00 USD | `-10.48%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 22,920.00 USD | 0.00 USD | 749.96 USD | `-10.26%` | `910.70` |
| `Live` | `Long` | `0.8365` | 22,170.00 USD | 0.00 USD | 316.70 USD | `-8.85%` | `378.60` |
| `Live` | `Long` | `0.8415` | 21,860.00 USD | 0.00 USD | 1,570.00 USD | `-8.30%` | `1,862.40` |
| `Live` | `Long` | `0.8435` | 20,290.00 USD | 0.00 USD | 895.29 USD | `-8.09%` | `1,061.40` |
| `Live` | `Long` | `0.8495` | 19,390.00 USD | 0.00 USD | 1,260.00 USD | `-7.43%` | `1,486.90` |
| `Live` | `Long` | `0.8515` | 18,130.00 USD | 0.00 USD | 2,700.00 USD | `-7.21%` | `3,175.90` |
| `Live` | `Long` | `0.8535` | 15,430.00 USD | 0.00 USD | 179.49 USD | `-7.00%` | `210.30` |
| `Live` | `Long` | `0.8575` | 15,250.00 USD | 0.00 USD | 620.32 USD | `-6.56%` | `723.40` |
| `Live` | `Long` | `0.8635` | 14,630.00 USD | 0.00 USD | 208.02 USD | `-5.91%` | `240.90` |
| `Live` | `Long` | `0.8645` | 14,420.00 USD | 0.00 USD | 438.30 USD | `-5.80%` | `507.00` |
| `Live` | `Long` | `0.8665` | 13,980.00 USD | 0.00 USD | 1,390.00 USD | `-5.58%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 12,590.00 USD | 0.00 USD | 12,590.00 USD | `-5.25%` | `14,478.80` |
| `Live` | `Short` | `0.9735` | 213.78 USD | 213.78 USD | 0.00 USD | `+6.08%` | `219.60` |
| `Live` | `Short` | `0.9795` | 9,070.00 USD | 8,850.00 USD | 0.00 USD | `+6.73%` | `9,038.80` |
| `Live` | `Short` | `0.9815` | 9,280.00 USD | 216.72 USD | 0.00 USD | `+6.95%` | `220.80` |
| `Live` | `Short` | `0.9985` | 9,500.00 USD | 220.47 USD | 0.00 USD | `+8.80%` | `220.80` |
| `Live` | `Short` | `1.00` | 9,730.00 USD | 220.91 USD | 0.00 USD | `+9.02%` | `220.80` |
| `Live` | `Short` | `1.01` | 9,950.00 USD | 221.13 USD | 0.00 USD | `+9.68%` | `219.70` |
| `Live` | `Short` | `1.04` | 10,170.00 USD | 228.37 USD | 0.00 USD | `+13.16%` | `219.90` |
| `Live` | `Short` | `1.05` | 10,540.00 USD | 367.04 USD | 0.00 USD | `+14.14%` | `350.40` |
| `Live` | `Short` | `1.05` | 10,840.00 USD | 298.35 USD | 0.00 USD | `+14.80%` | `283.20` |
| `Live` | `Short` | `1.08` | 13,070.00 USD | 2,230.00 USD | 0.00 USD | `+17.85%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 13,240.00 USD | 170.02 USD | 0.00 USD | `+21.01%` | `153.10` |
| `Live` | `Short` | `1.17` | 15,700.00 USD | 2,450.00 USD | 0.00 USD | `+27.55%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 37,880.00 USD | 22,180.00 USD | 0.00 USD | `+29.51%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 49,610.00 USD | 11,730.00 USD | 0.00 USD | `+44.22%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 49,850.00 USD | 239.77 USD | 0.00 USD | `+45.96%` | `179.00` |
| `Live` | `Short` | `1.42` | 53,040.00 USD | 3,190.00 USD | 0.00 USD | `+54.68%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 53,220.00 USD | 176.31 USD | 0.00 USD | `+68.08%` | `114.30` |
| `Live` | `Short` | `1.56` | 55,030.00 USD | 1,810.00 USD | 0.00 USD | `+69.61%` | `1,161.90` |
| `Live` | `Short` | `1.58` | 55,150.00 USD | 125.25 USD | 0.00 USD | `+71.68%` | `79.50` |
| `Live` | `Short` | `1.60` | 55,950.00 USD | 798.29 USD | 0.00 USD | `+74.19%` | `499.40` |
| `Live` | `Short` | `1.62` | 58,390.00 USD | 2,440.00 USD | 0.00 USD | `+77.02%` | `1,500.00` |
| `Live` | `Short` | `1.65` | 66,620.00 USD | 8,240.00 USD | 0.00 USD | `+79.52%` | `5,000.00` |
| `Live` | `Short` | `1.67` | 66,920.00 USD | 300.15 USD | 0.00 USD | `+81.70%` | `180.00` |
| `Live` | `Short` | `1.67` | 67,170.00 USD | 244.39 USD | 0.00 USD | `+82.03%` | `146.30` |
| `Live` | `Short` | `1.71` | 67,500.00 USD | 328.44 USD | 0.00 USD | `+86.50%` | `191.90` |
| `Live` | `Short` | `1.73` | 67,690.00 USD | 190.42 USD | 0.00 USD | `+88.46%` | `110.10` |
| `Live` | `Short` | `1.83` | 91,320.00 USD | 23,630.00 USD | 0.00 USD | `+99.36%` | `12,916.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 340,780.00 USD | 0.00 USD | 120.45 USD | `-56.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 340,660.00 USD | 0.00 USD | 150.15 USD | `-45.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 340,510.00 USD | 0.00 USD | 186.15 USD | `-40.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 340,320.00 USD | 0.00 USD | 1,150.00 USD | `-28.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 339,180.00 USD | 0.00 USD | 781.90 USD | `-23.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 338,390.00 USD | 0.00 USD | 477.38 USD | `-22.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 337,920.00 USD | 0.00 USD | 341.33 USD | `-21.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 337,580.00 USD | 0.00 USD | 972.82 USD | `-21.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 336,600.00 USD | 0.00 USD | 160.20 USD | `-20.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 336,440.00 USD | 0.00 USD | 102.58 USD | `-19.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 336,340.00 USD | 0.00 USD | 289.49 USD | `-18.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 336,050.00 USD | 0.00 USD | 197.53 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 335,850.00 USD | 0.00 USD | 14,570.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7855` | 321,290.00 USD | 0.00 USD | 213.58 USD | `-14.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 321,070.00 USD | 0.00 USD | 274,830.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 46,240.00 USD | 0.00 USD | 108.47 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8105` | 46,130.00 USD | 0.00 USD | 326.96 USD | `-11.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 45,800.00 USD | 0.00 USD | 405.75 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 45,400.00 USD | 0.00 USD | 772.84 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 44,620.00 USD | 0.00 USD | 2,670.00 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 41,950.00 USD | 0.00 USD | 3,470.00 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 38,480.00 USD | 0.00 USD | 9,180.00 USD | `-7.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 29,300.00 USD | 0.00 USD | 341.94 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 28,960.00 USD | 0.00 USD | 1,150.00 USD | `-6.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 27,810.00 USD | 0.00 USD | 429.25 USD | `-6.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 27,380.00 USD | 0.00 USD | 223.30 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 27,160.00 USD | 0.00 USD | 518.51 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8715` | 26,640.00 USD | 0.00 USD | 205.24 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 26,440.00 USD | 0.00 USD | 649.66 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 25,790.00 USD | 0.00 USD | 194.06 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 25,590.00 USD | 0.00 USD | 193.35 USD | `-3.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 25,400.00 USD | 0.00 USD | 223.04 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 25,180.00 USD | 0.00 USD | 10,840.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 14,330.00 USD | 0.00 USD | 4,920.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 9,420.00 USD | 0.00 USD | 317.02 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 9,100.00 USD | 0.00 USD | 192.07 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 8,910.00 USD | 0.00 USD | 195.32 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 8,710.00 USD | 0.00 USD | 196.87 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 8,510.00 USD | 0.00 USD | 2,870.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 5,640.00 USD | 0.00 USD | 795.32 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 4,840.00 USD | 0.00 USD | 398.91 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 4,450.00 USD | 0.00 USD | 196.96 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 4,250.00 USD | 0.00 USD | 300.38 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 3,950.00 USD | 0.00 USD | 198.61 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9075` | 3,750.00 USD | 0.00 USD | 994.35 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9085` | 2,760.00 USD | 0.00 USD | 363.40 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9095` | 2,390.00 USD | 0.00 USD | 198.18 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9115` | 2,190.00 USD | 0.00 USD | 397.23 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9135` | 1,800.00 USD | 0.00 USD | 398.65 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9145` | 1,400.00 USD | 0.00 USD | 399.09 USD | `-0.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9155` | 998.79 USD | 0.00 USD | 403.92 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9165` | 594.87 USD | 0.00 USD | 198.06 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9175` | 396.82 USD | 0.00 USD | 396.82 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 899.85 USD | 899.85 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 1,800.00 USD | 900.19 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 2,210.00 USD | 407.41 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 2,610.00 USD | 407.30 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 2,820.00 USD | 201.94 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9245` | 3,020.00 USD | 201.45 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 3,840.00 USD | 817.40 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9265` | 4,240.00 USD | 403.77 USD | 0.00 USD | `+0.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 6,360.00 USD | 2,120.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 6,600.00 USD | 246.05 USD | 0.00 USD | `+1.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 7,010.00 USD | 407.49 USD | 0.00 USD | `+1.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 7,210.00 USD | 203.97 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9315` | 7,480.00 USD | 263.80 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 7,720.00 USD | 241.98 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 8,540.00 USD | 814.76 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 8,740.00 USD | 201.97 USD | 0.00 USD | `+1.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 18,420.00 USD | 9,680.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 18,840.00 USD | 416.01 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 19,390.00 USD | 555.18 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 20,210.00 USD | 816.96 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 21,940.00 USD | 1,730.00 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 22,320.00 USD | 383.87 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 22,940.00 USD | 623.93 USD | 0.00 USD | `+3.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 23,360.00 USD | 414.68 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 23,740.00 USD | 381.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 25,760.00 USD | 2,020.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 25,960.00 USD | 206.77 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 26,200.00 USD | 236.26 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 26,340.00 USD | 136.83 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 26,600.00 USD | 261.16 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 28,500.00 USD | 1,910.00 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 29,070.00 USD | 568.75 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 29,240.00 USD | 163.29 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 29,620.00 USD | 385.74 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 31,660.00 USD | 2,030.00 USD | 0.00 USD | `+5.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 31,920.00 USD | 262.52 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 32,310.00 USD | 387.83 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 39,940.00 USD | 7,630.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 48,680.00 USD | 8,750.00 USD | 0.00 USD | `+6.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 70,650.00 USD | 21,960.00 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 71,040.00 USD | 396.17 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 71,720.00 USD | 676.53 USD | 0.00 USD | `+6.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 80,070.00 USD | 8,350.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 82,100.00 USD | 2,030.00 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 84,160.00 USD | 2,060.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 84,410.00 USD | 255.38 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 99,490.00 USD | 15,070.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 99,600.00 USD | 109.99 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 134,570.00 USD | 34,970.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 138,090.00 USD | 3,520.00 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 169,840.00 USD | 31,750.00 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 170,250.00 USD | 403.06 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 170,650.00 USD | 403.28 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 175,790.00 USD | 5,140.00 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 213,100.00 USD | 37,310.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 214,100.00 USD | 1,000.00 USD | 0.00 USD | `+9.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 254,700.00 USD | 40,590.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 254,930.00 USD | 235.79 USD | 0.00 USD | `+9.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 256,280.00 USD | 1,340.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 256,510.00 USD | 230.39 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 256,720.00 USD | 218.64 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 257,130.00 USD | 409.86 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 257,240.00 USD | 110.95 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 257,860.00 USD | 615.60 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 258,420.00 USD | 561.17 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 258,640.00 USD | 214.40 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 258,840.00 USD | 207.97 USD | 0.00 USD | `+11.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 259,050.00 USD | 208.26 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 259,570.00 USD | 516.75 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 259,920.00 USD | 348.86 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 260,310.00 USD | 391.80 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 260,720.00 USD | 413.76 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 261,080.00 USD | 354.91 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 262,980.00 USD | 1,900.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 263,190.00 USD | 207.87 USD | 0.00 USD | `+13.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 263,400.00 USD | 207.97 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 263,510.00 USD | 107.99 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 338,340.00 USD | 74,840.00 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 338,890.00 USD | 544.88 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 341,060.00 USD | 2,170.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 342,600.00 USD | 1,540.00 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 352,520.00 USD | 9,930.00 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 353,400.00 USD | 877.63 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 353,570.00 USD | 171.09 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 356,340.00 USD | 2,770.00 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 358,380.00 USD | 2,040.00 USD | 0.00 USD | `+22.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 358,570.00 USD | 187.56 USD | 0.00 USD | `+22.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 358,750.00 USD | 187.72 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 358,940.00 USD | 188.39 USD | 0.00 USD | `+23.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 361,610.00 USD | 2,670.00 USD | 0.00 USD | `+23.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 361,780.00 USD | 174.23 USD | 0.00 USD | `+23.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 361,960.00 USD | 174.38 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 362,130.00 USD | 174.84 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 362,280.00 USD | 150.90 USD | 0.00 USD | `+25.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 362,430.00 USD | 151.03 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 362,580.00 USD | 151.16 USD | 0.00 USD | `+25.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 362,740.00 USD | 151.29 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 362,890.00 USD | 151.42 USD | 0.00 USD | `+25.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 364,940.00 USD | 2,050.00 USD | 0.00 USD | `+27.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 365,050.00 USD | 110.00 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 365,520.00 USD | 475.80 USD | 0.00 USD | `+29.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 366,730.00 USD | 1,210.00 USD | 0.00 USD | `+30.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 409,660.00 USD | 42,930.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 411,660.00 USD | 2,000.00 USD | 0.00 USD | `+34.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 413,040.00 USD | 1,380.00 USD | 0.00 USD | `+36.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 413,290.00 USD | 245.41 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 421,680.00 USD | 8,390.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 422,100.00 USD | 415.25 USD | 0.00 USD | `+41.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 428,620.00 USD | 6,520.00 USD | 0.00 USD | `+42.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 433,410.00 USD | 4,800.00 USD | 0.00 USD | `+42.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 434,070.00 USD | 655.75 USD | 0.00 USD | `+42.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 434,660.00 USD | 596.43 USD | 0.00 USD | `+45.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 436,480.00 USD | 1,810.00 USD | 0.00 USD | `+46.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 450,360.00 USD | 13,880.00 USD | 0.00 USD | `+46.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 451,620.00 USD | 1,250.00 USD | 0.00 USD | `+47.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 453,680.00 USD | 2,070.00 USD | 0.00 USD | `+51.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 453,820.00 USD | 140.05 USD | 0.00 USD | `+52.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 453,980.00 USD | 160.42 USD | 0.00 USD | `+52.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 454,940.00 USD | 954.32 USD | 0.00 USD | `+53.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 489,110.00 USD | 34,170.00 USD | 0.00 USD | `+56.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 489,990.00 USD | 879.84 USD | 0.00 USD | `+62.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 493,040.00 USD | 3,050.00 USD | 0.00 USD | `+65.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 493,340.00 USD | 297.27 USD | 0.00 USD | `+69.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 501,870.00 USD | 8,530.00 USD | 0.00 USD | `+80.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 502,020.00 USD | 143.99 USD | 0.00 USD | `+81.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 502,190.00 USD | 177.05 USD | 0.00 USD | `+92.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 502,620.00 USD | 431.40 USD | 0.00 USD | `+96.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 502,850.00 USD | 220.77 USD | 0.00 USD | `+98.16%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `175.15M` | Total OI Tokens: `188,211,171.0 DOT`
  * 1h OI Change: `-10.62%` | 4h OI Change: `-9.62%` | 24h OI Change: `-15.85%`
  * Exchange Breakdown: Binance=`35.37M` | Bybit=`21.89M` | OKX=`10.38M` | Hyperliquid=`5.77M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.57K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0268%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0071%` |
| **USDT MEXC** | `0.0096%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0074%` | **USDT Bitget** | `-0.0018%` |
| **CoinM Binance** | `-0.0036%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `59.90%` | `40.10%` | `1.49` | 1,970,000.00 USD |
| `15M` | `Binance` | `53.03%` | `46.97%` | `1.13` | 817,370.00 USD |
| `15M` | `OKX` | `71.83%` | `28.17%` | `2.55` | 422,270.00 USD |
| `15M` | `Bybit` | `71.62%` | `28.38%` | `2.52` | 162,550.00 USD |
| `15M` | `KuCoin` | `49.89%` | `50.11%` | `1.00` | 145,710.00 USD |
| `15M` | `Gate` | `56.06%` | `43.94%` | `1.28` | 26,220.00 USD |
| `15M` | `Bitget` | `52.59%` | `47.41%` | `1.11` | 31,510.00 USD |
| `15M` | `BingX` | `58.22%` | `41.78%` | `1.39` | 130,340.00 USD |
| `15M` | `MEXC` | `48.11%` | `51.89%` | `0.93` | 63,260.00 USD |
| `15M` | `Bitunix` | `55.2%` | `44.8%` | `1.23` | 40,650.00 USD |
| `15M` | `Hyperliquid` | `80.29%` | `19.71%` | `4.07` | 21,630.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.01%` | `50.99%` | `0.96` | 62,680.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 48,070.00 USD |
| `15M` | `HTX` | `31.45%` | `68.55%` | `0.46` | 1,560.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `12.72%` | `87.28%` | `0.15` | 461.55 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `53.03%` | `46.97%` | `1.13` | 817,370.00 USD |
| `15M` | `Global Accounts` | `59.90%` | `40.10%` | `1.49` | 1,970,000.00 USD |
| `1H` | `DOT` | `53.58%` | `46.42%` | `1.15` | 7,410,000.00 USD |
| `1H` | `Binance` | `48.2%` | `51.8%` | `0.93` | 2,890,000.00 USD |
| `1H` | `OKX` | `66.37%` | `33.63%` | `1.97` | 911,460.00 USD |
| `1H` | `Bybit` | `67.62%` | `32.38%` | `2.09` | 512,370.00 USD |
| `1H` | `KuCoin` | `49.98%` | `50.02%` | `1.00` | 544,940.00 USD |
| `1H` | `Gate` | `49.6%` | `50.4%` | `0.98` | 214,160.00 USD |
| `1H` | `Bitget` | `51.23%` | `48.77%` | `1.05` | 240,930.00 USD |
| `1H` | `BingX` | `38.7%` | `61.3%` | `0.63` | 649,840.00 USD |
| `1H` | `MEXC` | `52.28%` | `47.72%` | `1.10` | 207,250.00 USD |
| `1H` | `Bitunix` | `51.71%` | `48.29%` | `1.07` | 167,290.00 USD |
| `1H` | `Hyperliquid` | `90.25%` | `9.75%` | `9.26` | 154,550.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.35%` | `50.65%` | `0.97` | 730,190.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.88%` | `0.12%` | `832.33` | 174,410.00 USD |
| `1H` | `HTX` | `30.91%` | `69.09%` | `0.45` | 2,750.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `100%` | `0%` | `1.00` | 2.74 USD |
| `1H` | `Aster` | `12.16%` | `87.84%` | `0.14` | 6,220.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `48.2%` | `51.8%` | `0.93` | 2,890,000.00 USD |
| `1H` | `Global Accounts` | `53.58%` | `46.42%` | `1.15` | 7,410,000.00 USD |
| `4H` | `DOT` | `51.59%` | `48.41%` | `1.07` | 526,360,000.00 USD |
| `4H` | `Binance` | `51.97%` | `48.03%` | `1.08` | 210,180,000.00 USD |
| `4H` | `OKX` | `53.24%` | `46.76%` | `1.14` | 61,880,000.00 USD |
| `4H` | `Bybit` | `48.69%` | `51.31%` | `0.95` | 68,490,000.00 USD |
| `4H` | `KuCoin` | `46.66%` | `53.34%` | `0.87` | 3,830,000.00 USD |
| `4H` | `Gate` | `57.62%` | `42.38%` | `1.36` | 17,370,000.00 USD |
| `4H` | `Bitget` | `45.27%` | `54.73%` | `0.83` | 25,460,000.00 USD |
| `4H` | `BingX` | `38.5%` | `61.5%` | `0.63` | 18,880,000.00 USD |
| `4H` | `MEXC` | `48.18%` | `51.82%` | `0.93` | 21,090,000.00 USD |
| `4H` | `Bitunix` | `50.64%` | `49.36%` | `1.03` | 9,040,000.00 USD |
| `4H` | `Hyperliquid` | `67.51%` | `32.49%` | `2.08` | 68,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.62%` | `50.38%` | `0.98` | 1,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 25,300.00 USD |
| `4H` | `WhiteBIT` | `94.6%` | `5.4%` | `17.52` | 8,350,000.00 USD |
| `4H` | `HTX` | `46.88%` | `53.12%` | `0.88` | 1,070,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.26%` | `53.74%` | `0.86` | 3,330,000.00 USD |
| `4H` | `Aster` | `32.89%` | `67.11%` | `0.49` | 3,600,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 3,550,000.00 USD |
| `4H` | `Whale Positions` | `51.97%` | `48.03%` | `1.08` | 210,180,000.00 USD |
| `4H` | `Global Accounts` | `51.59%` | `48.41%` | `1.07` | 526,360,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9111` | `0.9070` | `0.9111` | `0.9142` | `0.8973` | 1,250,275.83 USD | 633,543.99 USD | 616,731.85 USD | 16,812.14 USD | `+1.34%` | `19B / 16S` |
| `5:00 UTC` | `0.9049` | `0.9049` | `0.9049` | `0.9096` | `0.9016` | 668,740.93 USD | 336,954.59 USD | 331,786.34 USD | 5,168.25 USD | `+0.77%` | `7B / 15S` |
| `0:00 UTC` | `0.9041` | `0.9059` | `0.9041` | `0.9121` | `0.9022` | 1,124,680.00 USD | 451,427.52 USD | 673,252.48 USD | -221,824.96 USD | `-19.72%` | `19B / 6S` |
| `5:00 UTC` | `0.9141` | `0.9167` | `0.9141` | `0.9231` | `0.9118` | 773,293.12 USD | 467,556.11 USD | 305,737.01 USD | 161,819.09 USD | `+20.93%` | `24B / 7S` |
| `0:00 UTC` | `0.9221` | `0.9217` | `0.9221` | `0.9232` | `0.9187` | 866,180.64 USD | 516,857.79 USD | 349,322.85 USD | 167,534.95 USD | `+19.34%` | `5B / 8S` |
| `5:00 UTC` | `0.9201` | `0.9176` | `0.9201` | `0.9222` | `0.9147` | 486,388.28 USD | 243,662.09 USD | 242,726.19 USD | 935.89 USD | `+0.19%` | `11B / 18S` |
| `0:00 UTC` | `0.9193` | `0.9207` | `0.9193` | `0.9244` | `0.9172` | 1,009,160.47 USD | 369,502.50 USD | 639,657.97 USD | -270,155.47 USD | `-26.77%` | `7B / 22S` |
| `5:00 UTC` | `0.9247` | `0.9214` | `0.9247` | `0.9264` | `0.9171` | 592,145.67 USD | 331,376.92 USD | 260,768.76 USD | 70,608.16 USD | `+11.92%` | `20B / 3S` |
| `0:00 UTC` | `0.9301` | `0.9294` | `0.9301` | `0.9320` | `0.9246` | 722,739.41 USD | 436,845.68 USD | 285,893.73 USD | 150,951.95 USD | `+20.89%` | `15B / 5S` |
| `5:00 UTC` | `0.9322` | `0.9320` | `0.9322` | `0.9331` | `0.9309` | 109,241.44 USD | 50,742.06 USD | 58,499.38 USD | -7,757.33 USD | `-7.10%` | `1B / 3S` |

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
| `5m` | 19,770.00 USD | 112,960.00 USD | **`ACCUMULATION`** |
| `15m` | 37,290.00 USD | 394,390.00 USD | **`ACCUMULATION`** |
| `30m` | 29,330.00 USD | 567,880.00 USD | **`ACCUMULATION`** |
| `1h` | 2,520.00 USD | 333,490.00 USD | **`ACCUMULATION`** |
| `2h` | 63,460.00 USD | 875,890.00 USD | **`ACCUMULATION`** |
| `4h` | -217,190.00 USD | 1,640,000.00 USD | **`ACCUMULATION`** |
| `6h` | -109,910.00 USD | 1,300,000.00 USD | **`ACCUMULATION`** |
| `8h` | -1,000,000.00 USD | -4,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,060,000.00 USD | -5,490,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,040,000.00 USD | -6,290,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,480,000.00 USD | -23,430,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,720,000.00 USD | -77,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+19.77K` | 15m=`+37.29K` | 1h=`+2.52K` | 24h=`-1.04M`
* Futures Capital Netflows: 5m=`+112.96K` | 15m=`+394.39K` | 1h=`+333.49K` | 24h=`-6.29M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8923` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8493` (Risk Distance: `0.0430` pts)
  * +2.5R Take Profit: `0.9999`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9216` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9646` (Risk Distance: `0.0430` pts)
  * +2.5R Take Profit: `0.8140`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9395`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
