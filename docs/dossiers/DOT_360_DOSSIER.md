# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.8910` | **Live Ask Quote**: `0.9120` | **Mid Price**: `0.9015`
- **Spread Points**: `21.00` | **Spread BPS**: `232.95 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.8849` | VWAP Z-Score: `-1.18` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0134` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `39.22` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.06` | Lower -3.00σ Band: `0.8254`
  * Upper +2.51σ Band: `1.04` | Lower -2.51σ Band: `0.8447`
  * Upper +2.01σ Band: `1.02` | Lower -2.01σ Band: `0.8643`
  * Upper +2.00σ Band: `1.02` | Lower -2.00σ Band: `0.8647`
  * Upper +1.28σ Band: `0.9935` | Lower -1.28σ Band: `0.8930`
  * Upper +1.00σ Band: `0.9825` | Lower -1.00σ Band: `0.9039`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.8955` | EMA-20=`0.9081` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9352` (Slope: `+0.0000`) | EMA-100=`0.9543`
  * Institutional Anchors: EMA-144=`0.9622` | EMA-200=`0.9674` (Slope: `-0.9242`) | EMA-233=`0.9712`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9216` (Distance: `-2.13%`)
  * Point of Control (POC) = `0.9121` (Distance: `-1.11%`)
  * Value Area Low (VAL) = `0.8890` (Distance: `+1.47%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9945` | Weekly VAL=`0.9724`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9051` | Low=`0.8979`
  * New York Session (13:00-21:00 UTC): High=`0.9069` | Low=`0.8961`
  * Initial Balance (First Hour): IB High=`0.9042` | IB Low=`0.8988`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.8979` - `0.9051`
  * Optimal Trade Entry (OTE 0.705): `0.9033`
  * Structural Invalidation Anchor (0.786): `0.9087`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9088` | `0.9096` | `0.9034` | `0.9062` | `240,347` | 217,744.08 USD | 2,554.50 USD | `+1.17%` | -3,202,866.39 USD | `-0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.9063` | `0.9065` | `0.9016` | `0.9040` | `191,048` | 172,619.04 USD | -6,069.55 USD | `-3.52%` | -3,208,935.95 USD | `-0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.9041` | `0.9054` | `0.9026` | `0.9030` | `120,840` | 109,239.06 USD | 12,175.14 USD | `+11.15%` | -3,196,760.81 USD | `-0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9115` | `0.9119` | `0.9046` | `0.9054` | `1,094,163` | 994,017.98 USD | 150,556.98 USD | `+15.15%` | -3,222,233.03 USD | `+0.39` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9053` | `0.9141` | `0.8973` | `0.9088` | `1,378,655` | 1,250,275.83 USD | 16,812.14 USD | `+1.34%` | -3,205,420.89 USD | `+0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9088` | `0.9096` | `0.9016` | `0.9034` | `553,378` | 500,634.27 USD | 9,692.17 USD | `+1.94%` | -3,195,728.72 USD | `+0.01` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.9241` | `0.9248` | `0.9075` | `0.9088` | `4,418,502` | 4,047,635.87 USD | -427,037.19 USD | `-10.55%` | -4,591,084.78 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.9089` | `0.9105` | `0.8671` | `0.8988` | `11,929,789` | 10,597,351.48 USD | -934,371.84 USD | `-8.82%` | -5,525,456.62 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8988` | `0.9187` | `0.8939` | `0.9030` | `8,881,327` | 8,053,455.22 USD | 2,328,695.81 USD | `+28.92%` | -3,196,760.81 USD | `+2.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -876,375.92 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,401,104.65 USD | `-1.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9187` | `0.8671` | `0.9030` | `20,811,117` | 18,650,806.69 USD | 1,394,323.97 USD | `+7.48%` | -4,006,780.67 USD | `+1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 98,266.33 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -79,310.47 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -876,375.92 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,401,104.65 USD | `-1.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9187` | `0.8671` | `0.9030` | `20,811,117` | 18,650,806.69 USD | 1,394,323.97 USD | `+7.48%` | -4,006,780.67 USD | `+1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.9015`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.02` | 5,545.81 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 5.55K USD at 1.0190 USD [API] | `2026-10-28 22:45:22` |
| `ANNOUNCEMENT` | `INFO` | `1.02` | 6,059.91 USD | `-` | `NEWS_INTEL` | `-` | #DOT Whale BUY: 6.06K USD at 1.0189 USD [API] | `2026-10-28 22:45:22` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.9461` (Vol: 248,700.00 USD, Dist: `+2.77%`) | Long MP=`0.9083` (Vol: 248,700.00 USD, Dist: `--1.33%`)
  * 48H Horizon: Short MP=`0.9463` (Vol: 248,700.00 USD, Dist: `+2.79%`) | Long MP=`0.9085` (Vol: 248,700.00 USD, Dist: `--1.32%`)
  * 3D Horizon: Short MP=`0.9463` (Vol: 248,700.00 USD, Dist: `+2.79%`) | Long MP=`0.9085` (Vol: 248,700.00 USD, Dist: `--1.32%`)
  * 7D Horizon: Short MP=`0.9460` (Vol: 248,700.00 USD, Dist: `+2.76%`) | Long MP=`0.9102` (Vol: 172,900.00 USD, Dist: `--1.13%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2245` | 112.25 USD | 356,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3555` | 785.30 USD | 355,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4095` | 30,710.00 USD | 355,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 324,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4295` | 2,450.00 USD | 321,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 1,170.00 USD | 319,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 3,390.00 USD | 318,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 314,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5115` | 606.38 USD | 311,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 4,130.00 USD | 310,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5235` | 211.34 USD | 306,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 306,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5795` | 229.77 USD | 305,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 305,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 304,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5925` | 35,550.00 USD | 304,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 2,260.00 USD | 269,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 266,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 265,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 265,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 264,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 264,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 264,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 261,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6425` | 104.60 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 20,920.00 USD | 241,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 220,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6515` | 576.71 USD | 220,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 413.70 USD | 219,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6715` | 214.41 USD | 219,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6725` | 63,890.00 USD | 219,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 155,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 154,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6955` | 322.16 USD | 154,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 154,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7035` | 214.15 USD | 152,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7075` | 16,520.00 USD | 152,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 136,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 135,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 133,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7255` | 1,090.00 USD | 133,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 132,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,300.00 USD | 131,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 129,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7365` | 164.53 USD | 128,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7375` | 737.50 USD | 128,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 127,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7415` | 52,650.00 USD | 127,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 74,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 74,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 144.07 USD | 72,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7605` | 834.88 USD | 72,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7615` | 804.07 USD | 71,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 71,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7765` | 1,010.00 USD | 67,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7785` | 210.58 USD | 66,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7815` | 234.45 USD | 66,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 65,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,090,000.00 USD | 2,090,000.00 USD | 7,140.00 USD | 2,140.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7910` | 2,080,000.00 USD | 2,080,000.00 USD | 11,460.00 USD | 3,680.00 USD | 8,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7930` | 2,060,000.00 USD | 2,060,000.00 USD | 20,360.00 USD | 1,170.00 USD | 6,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7950` | 2,030,000.00 USD | 2,030,000.00 USD | 3,290.00 USD | 4,820.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7970` | 2,010,000.00 USD | 2,010,000.00 USD | 10,100.00 USD | 933.42 USD | 522.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.7990` | 2,000,000.00 USD | 2,000,000.00 USD | 20,360.00 USD | 6,210.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8010` | 1,950,000.00 USD | 1,950,000.00 USD | 5,420.00 USD | 5,200.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8025` | 238.90 USD | 65,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8030` | 1,940,000.00 USD | 1,940,000.00 USD | 4,550.00 USD | 2,260.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8050` | 1,930,000.00 USD | 1,930,000.00 USD | 9,820.00 USD | 8,430.00 USD | 3,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8070` | 1,900,000.00 USD | 1,900,000.00 USD | 12,160.00 USD | 4,930.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8090` | 1,880,000.00 USD | 1,880,000.00 USD | 1,100.00 USD | 1,960.00 USD | 4,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8105` | 13,410.00 USD | 65,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8110` | 1,870,000.00 USD | 1,870,000.00 USD | 7,910.00 USD | 102.12 USD | 340.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8130` | 1,860,000.00 USD | 1,860,000.00 USD | 14,060.00 USD | 2,950.00 USD | 8,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 51,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,840,000.00 USD | 1,840,000.00 USD | 5,990.00 USD | 7,610.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,820,000.00 USD | 1,820,000.00 USD | 10,780.00 USD | 2,370.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8185` | 200.21 USD | 51,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,800,000.00 USD | 1,800,000.00 USD | 8,920.00 USD | 2,530.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,780,000.00 USD | 1,780,000.00 USD | 7,510.00 USD | 3,060.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 51,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,760,000.00 USD | 1,760,000.00 USD | 29,430.00 USD | 4,660.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 49,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 48,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,640,000.00 USD | 1,640,000.00 USD | 15,240.00 USD | 154.74 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 1,370,000.00 USD | 1,370,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 1,360,000.00 USD | 1,360,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,620,000.00 USD | 1,620,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,240.00 USD | 48,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,610,000.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,620.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8440` | 1,360,000.00 USD | 1,360,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 474.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8455` | 706.50 USD | 46,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,600,000.00 USD | 1,600,000.00 USD | 7,900.00 USD | 1,130.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,590,000.00 USD | 1,590,000.00 USD | 731.45 USD | 132.08 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 46,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 1,350,000.00 USD | 1,350,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,590,000.00 USD | 1,590,000.00 USD | 5,480.00 USD | 114.10 USD | 4,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,580,000.00 USD | 1,580,000.00 USD | 2,130.00 USD | 2,670.00 USD | 1,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8540` | 1,350,000.00 USD | 1,350,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8550` | 1,570,000.00 USD | 1,570,000.00 USD | 254.55 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8560` | 1,350,000.00 USD | 1,350,000.00 USD | 2,270.00 USD | 199.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8570` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 944.22 USD | 577.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8575` | 620.32 USD | 44,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8580` | 1,340,000.00 USD | 1,340,000.00 USD | 617.52 USD | 197.60 USD | 182.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8590` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 211.77 USD | 1,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8600` | 1,340,000.00 USD | 1,340,000.00 USD | 6,520.00 USD | 1,220.00 USD | 251.39 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8605` | 127.01 USD | 44,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8610` | 1,560,000.00 USD | 1,560,000.00 USD | 7,320.00 USD | 2,920.00 USD | 467.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8620` | 1,340,000.00 USD | 1,340,000.00 USD | 7,410.00 USD | 70.98 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8625` | 309.55 USD | 44,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8630` | 1,550,000.00 USD | 1,550,000.00 USD | 758.91 USD | 2,820.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8635` | 208.02 USD | 43,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8640` | 1,330,000.00 USD | 1,330,000.00 USD | 6,350.00 USD | 2,070.00 USD | 3,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8645` | 438.30 USD | 43,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8650` | 1,550,000.00 USD | 1,550,000.00 USD | 6,720.00 USD | 0.00 USD | 184.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8660` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 20.18 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8665` | 1,390.00 USD | 43,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8670` | 1,540,000.00 USD | 1,540,000.00 USD | 12,100.00 USD | 3,240.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8680` | 1,320,000.00 USD | 1,320,000.00 USD | 3,580.00 USD | 3,640.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8690` | 1,520,000.00 USD | 1,520,000.00 USD | 25,250.00 USD | 2,030.00 USD | 8,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8695` | 12,590.00 USD | 41,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8700` | 1,300,000.00 USD | 1,300,000.00 USD | 21,490.00 USD | 3,580.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8710` | 1,480,000.00 USD | 1,480,000.00 USD | 7,370.00 USD | 1,110.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8720` | 1,270,000.00 USD | 1,270,000.00 USD | 32,240.00 USD | 26.70 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8730` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 2,080.00 USD | 295.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8740` | 1,230,000.00 USD | 1,230,000.00 USD | 7,270.00 USD | 3,350.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8750` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 583.80 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8760` | 1,220,000.00 USD | 1,220,000.00 USD | 17,510.00 USD | 3,760.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8765` | 171.88 USD | 29,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8770` | 1,450,000.00 USD | 1,450,000.00 USD | 52,140.00 USD | 15,830.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8780` | 1,190,000.00 USD | 1,190,000.00 USD | 24,840.00 USD | 15,580.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8790` | 1,380,000.00 USD | 1,380,000.00 USD | 873.30 USD | 3,920.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8795` | 948.01 USD | 28,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8800` | 1,120,000.00 USD | 1,120,000.00 USD | 47,770.00 USD | 13,000.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8810` | 1,370,000.00 USD | 1,370,000.00 USD | 228.30 USD | 53.23 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8815` | 27,450.00 USD | 28,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8820` | 1,060,000.00 USD | 1,060,000.00 USD | 11,810.00 USD | 13,820.00 USD | 425.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8830` | 1,370,000.00 USD | 1,370,000.00 USD | 8,430.00 USD | 6,110.00 USD | 957.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8840` | 1,030,000.00 USD | 1,030,000.00 USD | 11,270.00 USD | 3,590.00 USD | 1,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8845` | 549.72 USD | 549.72 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `0.9685` | 211.13 USD | 211.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9690` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 19,330.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,680,000.00 USD | 1,680,000.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,180,000.00 USD | 2,180,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,730,000.00 USD | 1,730,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,810,000.00 USD | 1,810,000.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,300,000.00 USD | 2,300,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,870,000.00 USD | 1,870,000.00 USD | 39,980.00 USD | 3,080.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9795` | 212.26 USD | 423.39 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,930,000.00 USD | 1,930,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9805` | 212.47 USD | 635.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,510,000.00 USD | 2,510,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,960,000.00 USD | 1,960,000.00 USD | 16,350.00 USD | 12,360.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,680,000.00 USD | 2,680,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 2,010,000.00 USD | 2,010,000.00 USD | 665.59 USD | 13,370.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,000.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9860` | 2,090,000.00 USD | 2,090,000.00 USD | 50,550.00 USD | 3,510.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,800,000.00 USD | 2,800,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9875` | 213.30 USD | 849.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9880` | 2,120,000.00 USD | 2,120,000.00 USD | 17,200.00 USD | 130.81 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,820,000.00 USD | 2,820,000.00 USD | 20,530.00 USD | 284.26 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 2,190,000.00 USD | 2,190,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 2,220,000.00 USD | 2,220,000.00 USD | 9,210.00 USD | 2,900.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9925` | 216.96 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 2,240,000.00 USD | 2,240,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,920,000.00 USD | 2,920,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9955` | 214.83 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9960` | 2,270,000.00 USD | 2,270,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 3,000,000.00 USD | 3,000,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 2,320,000.00 USD | 2,320,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9990` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 104.05 USD | 462.12 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9995` | 216.59 USD | 1,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 216.81 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,050,000.00 USD | 3,050,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,200,000.00 USD | 3,200,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,440,000.00 USD | 2,440,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.00` | 217.47 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,230,000.00 USD | 3,230,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `1.02` | 222.21 USD | 2,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `7D` | `Short Liquidation` | `1.04` | 6,030,000.00 USD | 6,030,000.00 USD | 239,580.00 USD | 8,210.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,930,000.00 USD | 6,930,000.00 USD | 184,670.00 USD | 23,680.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,450,000.00 USD | 7,450,000.00 USD | 178,890.00 USD | 96,750.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,650,000.00 USD | 7,650,000.00 USD | 116,670.00 USD | 13,190.00 USD | 77,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,960,000.00 USD | 7,960,000.00 USD | 175,350.00 USD | 43,000.00 USD | 87,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 1,450.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.07` | 12,350.00 USD | 16,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,000,000.00 USD | 11,000,000.00 USD | 96,630.00 USD | 43,620.00 USD | 95,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.07` | 11,190,000.00 USD | 11,190,000.00 USD | 97,650.00 USD | 27,650.00 USD | 60,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,340,000.00 USD | 11,340,000.00 USD | 75,040.00 USD | 29,740.00 USD | 48,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,580,000.00 USD | 11,580,000.00 USD | 166,380.00 USD | 21,770.00 USD | 52,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.08` | 11,810,000.00 USD | 11,810,000.00 USD | 164,440.00 USD | 26,210.00 USD | 33,950.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 16,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.15` | 1,500.00 USD | 17,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 20,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 42,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.24` | 1,070.00 USD | 43,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.26` | 250.37 USD | 43,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 55,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 55,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 59,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 513,610.00 USD | 572,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 572,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 574,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 124.14 USD | 574,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 782.81 USD | 575,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 235.18 USD | 575,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 578,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 586,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 318.46 USD | 586,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 587,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 31,120.00 USD | 618,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 90,940.00 USD | 709,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2265` | 293,930.00 USD | 0.00 USD | 113.25 USD | `-74.81%` | `500.00` |
| `Live` | `Long` | `0.2435` | 293,820.00 USD | 0.00 USD | 2,230.00 USD | `-72.92%` | `9,174.90` |
| `Live` | `Long` | `0.3255` | 291,580.00 USD | 0.00 USD | 558.40 USD | `-63.81%` | `1,715.50` |
| `Live` | `Long` | `0.3685` | 291,030.00 USD | 0.00 USD | 814.02 USD | `-59.02%` | `2,209.00` |
| `Live` | `Long` | `0.3855` | 290,210.00 USD | 0.00 USD | 314.45 USD | `-57.13%` | `815.70` |
| `Live` | `Long` | `0.4185` | 289,900.00 USD | 0.00 USD | 2,790.00 USD | `-53.46%` | `6,675.20` |
| `Live` | `Long` | `0.4645` | 287,100.00 USD | 0.00 USD | 2,960.00 USD | `-48.35%` | `6,377.30` |
| `Live` | `Long` | `0.4695` | 284,140.00 USD | 0.00 USD | 2,580.00 USD | `-47.79%` | `5,500.00` |
| `Live` | `Long` | `0.4715` | 281,560.00 USD | 0.00 USD | 161.49 USD | `-47.57%` | `342.50` |
| `Live` | `Long` | `0.5065` | 281,400.00 USD | 0.00 USD | 3,290.00 USD | `-43.68%` | `6,504.70` |
| `Live` | `Long` | `0.5585` | 278,100.00 USD | 0.00 USD | 41,890.00 USD | `-37.90%` | `75,000.00` |
| `Live` | `Long` | `0.5635` | 236,220.00 USD | 0.00 USD | 563.50 USD | `-37.34%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 235,650.00 USD | 0.00 USD | 14,600.00 USD | `-37.12%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 221,050.00 USD | 0.00 USD | 577.36 USD | `-36.67%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 220,480.00 USD | 0.00 USD | 683.51 USD | `-35.01%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 219,790.00 USD | 0.00 USD | 137.53 USD | `-34.45%` | `233.30` |
| `Live` | `Long` | `0.6055` | 219,650.00 USD | 0.00 USD | 2,260.00 USD | `-32.67%` | `3,731.20` |
| `Live` | `Long` | `0.6065` | 217,390.00 USD | 0.00 USD | 1,800.00 USD | `-32.56%` | `2,971.80` |
| `Live` | `Long` | `0.6115` | 215,590.00 USD | 0.00 USD | 242.46 USD | `-32.00%` | `396.50` |
| `Live` | `Long` | `0.6125` | 215,350.00 USD | 0.00 USD | 105.96 USD | `-31.89%` | `173.00` |
| `Live` | `Long` | `0.6145` | 215,240.00 USD | 0.00 USD | 147.48 USD | `-31.67%` | `240.00` |
| `Live` | `Long` | `0.6245` | 215,100.00 USD | 0.00 USD | 101.04 USD | `-30.56%` | `161.80` |
| `Live` | `Long` | `0.6265` | 215,000.00 USD | 0.00 USD | 1,100.00 USD | `-30.34%` | `1,749.80` |
| `Live` | `Long` | `0.6315` | 213,900.00 USD | 0.00 USD | 757.80 USD | `-29.78%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 213,140.00 USD | 0.00 USD | 106.00 USD | `-29.33%` | `166.80` |
| `Live` | `Long` | `0.6405` | 213,040.00 USD | 0.00 USD | 2,090.00 USD | `-28.78%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 210,950.00 USD | 0.00 USD | 20,270.00 USD | `-28.67%` | `31,595.60` |
| `Live` | `Long` | `0.6425` | 190,680.00 USD | 0.00 USD | 104.60 USD | `-28.56%` | `162.80` |
| `Live` | `Long` | `0.6465` | 190,570.00 USD | 0.00 USD | 4,230.00 USD | `-28.11%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 186,350.00 USD | 0.00 USD | 202.47 USD | `-28.00%` | `312.70` |
| `Live` | `Long` | `0.6595` | 186,140.00 USD | 0.00 USD | 149.44 USD | `-26.67%` | `226.60` |
| `Live` | `Long` | `0.6775` | 185,990.00 USD | 0.00 USD | 423.10 USD | `-24.66%` | `624.50` |
| `Live` | `Long` | `0.6835` | 185,570.00 USD | 0.00 USD | 512.97 USD | `-24.00%` | `750.50` |
| `Live` | `Long` | `0.6865` | 185,060.00 USD | 0.00 USD | 68,650.00 USD | `-23.66%` | `100,000.00` |
| `Live` | `Long` | `0.6885` | 116,410.00 USD | 0.00 USD | 19,720.00 USD | `-23.44%` | `28,635.00` |
| `Live` | `Long` | `0.6955` | 96,690.00 USD | 0.00 USD | 322.16 USD | `-22.66%` | `463.20` |
| `Live` | `Long` | `0.7005` | 96,370.00 USD | 0.00 USD | 1,140.00 USD | `-22.11%` | `1,634.20` |
| `Live` | `Long` | `0.7145` | 95,230.00 USD | 0.00 USD | 988.87 USD | `-20.55%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 94,240.00 USD | 0.00 USD | 1,580.00 USD | `-19.77%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 92,660.00 USD | 0.00 USD | 397.93 USD | `-19.55%` | `550.00` |
| `Live` | `Long` | `0.7275` | 92,260.00 USD | 0.00 USD | 162.52 USD | `-19.10%` | `223.40` |
| `Live` | `Long` | `0.7285` | 92,100.00 USD | 0.00 USD | 291.18 USD | `-18.99%` | `399.70` |
| `Live` | `Long` | `0.7305` | 91,800.00 USD | 0.00 USD | 2,300.00 USD | `-18.77%` | `3,143.00` |
| `Live` | `Long` | `0.7335` | 89,510.00 USD | 0.00 USD | 1,140.00 USD | `-18.44%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 88,370.00 USD | 0.00 USD | 283.30 USD | `-17.77%` | `383.10` |
| `Live` | `Long` | `0.7455` | 88,080.00 USD | 0.00 USD | 52,930.00 USD | `-17.10%` | `71,003.30` |
| `Live` | `Long` | `0.7525` | 35,150.00 USD | 0.00 USD | 331.18 USD | `-16.32%` | `440.10` |
| `Live` | `Long` | `0.7535` | 34,820.00 USD | 0.00 USD | 1,400.00 USD | `-16.21%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 33,420.00 USD | 0.00 USD | 446.80 USD | `-15.99%` | `591.40` |
| `Live` | `Long` | `0.7725` | 32,970.00 USD | 0.00 USD | 3,840.00 USD | `-14.10%` | `4,968.90` |
| `Live` | `Long` | `0.7795` | 29,130.00 USD | 0.00 USD | 272.83 USD | `-13.32%` | `350.00` |
| `Live` | `Long` | `0.7835` | 28,860.00 USD | 0.00 USD | 5,620.00 USD | `-12.88%` | `7,176.90` |
| `Live` | `Long` | `0.7865` | 23,240.00 USD | 0.00 USD | 292.03 USD | `-12.54%` | `371.30` |
| `Live` | `Long` | `0.7905` | 22,940.00 USD | 0.00 USD | 277.39 USD | `-12.10%` | `350.90` |
| `Live` | `Long` | `0.8135` | 22,670.00 USD | 0.00 USD | 647.79 USD | `-9.54%` | `796.30` |
| `Live` | `Long` | `0.8215` | 22,020.00 USD | 0.00 USD | 1,950.00 USD | `-8.65%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 20,070.00 USD | 0.00 USD | 749.96 USD | `-8.43%` | `910.70` |
| `Live` | `Long` | `0.8295` | 19,320.00 USD | 0.00 USD | 781.89 USD | `-7.76%` | `942.60` |
| `Live` | `Long` | `0.8365` | 18,540.00 USD | 0.00 USD | 316.70 USD | `-6.98%` | `378.60` |
| `Live` | `Long` | `0.8415` | 18,220.00 USD | 0.00 USD | 1,570.00 USD | `-6.43%` | `1,862.40` |
| `Live` | `Long` | `0.8435` | 16,650.00 USD | 0.00 USD | 143.90 USD | `-6.21%` | `170.60` |
| `Live` | `Long` | `0.8495` | 16,510.00 USD | 0.00 USD | 1,260.00 USD | `-5.54%` | `1,486.90` |
| `Live` | `Long` | `0.8575` | 15,250.00 USD | 0.00 USD | 620.32 USD | `-4.65%` | `723.40` |
| `Live` | `Long` | `0.8635` | 14,630.00 USD | 0.00 USD | 208.02 USD | `-3.98%` | `240.90` |
| `Live` | `Long` | `0.8645` | 14,420.00 USD | 0.00 USD | 438.30 USD | `-3.87%` | `507.00` |
| `Live` | `Long` | `0.8665` | 13,980.00 USD | 0.00 USD | 1,390.00 USD | `-3.65%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 12,590.00 USD | 0.00 USD | 12,590.00 USD | `-3.31%` | `14,478.80` |
| `Live` | `Short` | `0.9695` | 13,050.00 USD | 13,050.00 USD | 0.00 USD | `+7.80%` | `13,459.40` |
| `Live` | `Short` | `1.05` | 13,420.00 USD | 367.04 USD | 0.00 USD | `+16.48%` | `350.40` |
| `Live` | `Short` | `1.08` | 15,650.00 USD | 2,230.00 USD | 0.00 USD | `+20.26%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 15,820.00 USD | 169.86 USD | 0.00 USD | `+23.37%` | `153.10` |
| `Live` | `Short` | `1.17` | 18,270.00 USD | 2,450.00 USD | 0.00 USD | `+30.16%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 40,450.00 USD | 22,180.00 USD | 0.00 USD | `+32.16%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 52,180.00 USD | 11,730.00 USD | 0.00 USD | `+47.17%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 52,420.00 USD | 239.77 USD | 0.00 USD | `+48.95%` | `179.00` |
| `Live` | `Short` | `1.37` | 55,490.00 USD | 3,070.00 USD | 0.00 USD | `+52.06%` | `2,243.60` |
| `Live` | `Short` | `1.42` | 58,690.00 USD | 3,190.00 USD | 0.00 USD | `+57.84%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 58,860.00 USD | 176.31 USD | 0.00 USD | `+71.52%` | `114.30` |
| `Live` | `Short` | `1.56` | 60,670.00 USD | 1,810.00 USD | 0.00 USD | `+73.08%` | `1,161.90` |
| `Live` | `Short` | `1.59` | 61,460.00 USD | 794.30 USD | 0.00 USD | `+76.86%` | `499.40` |
| `Live` | `Short` | `1.62` | 63,900.00 USD | 2,440.00 USD | 0.00 USD | `+80.64%` | `1,500.00` |
| `Live` | `Short` | `1.63` | 64,030.00 USD | 129.94 USD | 0.00 USD | `+81.75%` | `79.50` |
| `Live` | `Short` | `1.65` | 72,270.00 USD | 8,240.00 USD | 0.00 USD | `+83.20%` | `5,000.00` |
| `Live` | `Short` | `1.66` | 72,510.00 USD | 242.93 USD | 0.00 USD | `+84.64%` | `146.30` |
| `Live` | `Short` | `1.67` | 72,810.00 USD | 300.15 USD | 0.00 USD | `+85.42%` | `180.00` |
| `Live` | `Short` | `1.72` | 73,140.00 USD | 329.40 USD | 0.00 USD | `+90.87%` | `191.90` |
| `Live` | `Short` | `1.73` | 73,330.00 USD | 190.42 USD | 0.00 USD | `+92.31%` | `110.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 323,620.00 USD | 0.00 USD | 120.45 USD | `-55.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 323,500.00 USD | 0.00 USD | 150.15 USD | `-44.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 323,350.00 USD | 0.00 USD | 186.15 USD | `-39.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 323,170.00 USD | 0.00 USD | 1,150.00 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 322,020.00 USD | 0.00 USD | 781.90 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 321,240.00 USD | 0.00 USD | 477.38 USD | `-20.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 320,760.00 USD | 0.00 USD | 341.33 USD | `-19.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 320,420.00 USD | 0.00 USD | 972.82 USD | `-19.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 319,450.00 USD | 0.00 USD | 160.20 USD | `-18.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 319,290.00 USD | 0.00 USD | 102.58 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 319,180.00 USD | 0.00 USD | 289.49 USD | `-16.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 318,890.00 USD | 0.00 USD | 197.53 USD | `-15.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 318,700.00 USD | 0.00 USD | 14,570.00 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 304,130.00 USD | 0.00 USD | 274,830.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 29,300.00 USD | 0.00 USD | 108.47 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 29,190.00 USD | 0.00 USD | 405.75 USD | `-9.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 28,780.00 USD | 0.00 USD | 772.84 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 28,010.00 USD | 0.00 USD | 3,470.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 24,540.00 USD | 0.00 USD | 9,180.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 15,360.00 USD | 0.00 USD | 341.94 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 15,020.00 USD | 0.00 USD | 1,150.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 13,870.00 USD | 0.00 USD | 429.25 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 13,440.00 USD | 0.00 USD | 223.30 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 13,220.00 USD | 0.00 USD | 518.51 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 12,700.00 USD | 0.00 USD | 649.66 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 12,050.00 USD | 0.00 USD | 193.35 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 11,860.00 USD | 0.00 USD | 223.04 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 11,630.00 USD | 0.00 USD | 10,840.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 788.40 USD | 0.00 USD | 158.51 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 629.89 USD | 0.00 USD | 192.07 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 437.82 USD | 0.00 USD | 195.32 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 242.50 USD | 0.00 USD | 242.50 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9035` | 196.96 USD | 196.96 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9045` | 497.35 USD | 300.38 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9065` | 695.96 USD | 198.61 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 1,690.00 USD | 994.35 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 2,050.00 USD | 363.40 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 2,450.00 USD | 398.72 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 2,650.00 USD | 199.80 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 2,850.00 USD | 199.49 USD | 0.00 USD | `+1.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 3,050.00 USD | 198.06 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 3,450.00 USD | 396.82 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 4,350.00 USD | 899.85 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 5,250.00 USD | 900.19 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 7,310.00 USD | 2,070.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 7,960.00 USD | 644.68 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 8,160.00 USD | 201.94 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 10,280.00 USD | 2,120.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 10,520.00 USD | 246.05 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 10,930.00 USD | 407.49 USD | 0.00 USD | `+3.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 11,130.00 USD | 203.97 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 11,380.00 USD | 241.98 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 11,580.00 USD | 201.64 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 11,780.00 USD | 201.97 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 21,460.00 USD | 9,680.00 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 21,880.00 USD | 416.01 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 22,440.00 USD | 555.18 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 23,250.00 USD | 816.96 USD | 0.00 USD | `+4.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 24,980.00 USD | 1,730.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 25,360.00 USD | 383.87 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 26,180.00 USD | 817.40 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 26,590.00 USD | 414.68 USD | 0.00 USD | `+5.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 26,980.00 USD | 381.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 28,990.00 USD | 2,020.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 29,200.00 USD | 206.77 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 29,440.00 USD | 236.26 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 29,570.00 USD | 136.83 USD | 0.00 USD | `+6.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 29,950.00 USD | 376.80 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 31,860.00 USD | 1,910.00 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 32,420.00 USD | 568.75 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 32,590.00 USD | 163.29 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9665` | 33,140.00 USD | 554.58 USD | 0.00 USD | `+7.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 33,530.00 USD | 385.74 USD | 0.00 USD | `+7.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 35,560.00 USD | 2,030.00 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 35,820.00 USD | 262.52 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 46,190.00 USD | 10,370.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 46,580.00 USD | 387.83 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 54,210.00 USD | 7,630.00 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 62,960.00 USD | 8,750.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 84,920.00 USD | 21,960.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 85,320.00 USD | 396.17 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 85,990.00 USD | 676.53 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 94,350.00 USD | 8,350.00 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 96,370.00 USD | 2,030.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 98,430.00 USD | 2,060.00 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 98,690.00 USD | 255.38 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 113,760.00 USD | 15,070.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 113,870.00 USD | 109.99 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 148,840.00 USD | 34,970.00 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 152,360.00 USD | 3,520.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 184,110.00 USD | 31,750.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 184,520.00 USD | 403.06 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 184,920.00 USD | 403.28 USD | 0.00 USD | `+10.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 190,060.00 USD | 5,140.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 227,370.00 USD | 37,310.00 USD | 0.00 USD | `+11.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 228,370.00 USD | 1,000.00 USD | 0.00 USD | `+11.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 268,970.00 USD | 40,590.00 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 269,200.00 USD | 235.79 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 270,550.00 USD | 1,340.00 USD | 0.00 USD | `+11.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 270,780.00 USD | 230.39 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 271,000.00 USD | 218.64 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 271,410.00 USD | 409.86 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 271,520.00 USD | 110.95 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 272,130.00 USD | 615.60 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 272,690.00 USD | 561.17 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 272,800.00 USD | 103.07 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 273,000.00 USD | 207.97 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 273,210.00 USD | 208.26 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 273,730.00 USD | 516.75 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 273,930.00 USD | 204.93 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 274,280.00 USD | 348.86 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 274,660.00 USD | 376.25 USD | 0.00 USD | `+15.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 275,070.00 USD | 413.76 USD | 0.00 USD | `+15.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 275,430.00 USD | 354.91 USD | 0.00 USD | `+15.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 277,330.00 USD | 1,900.00 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 277,540.00 USD | 207.87 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 277,750.00 USD | 207.97 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 279,040.00 USD | 1,290.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 279,250.00 USD | 206.97 USD | 0.00 USD | `+16.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 279,360.00 USD | 107.99 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 279,600.00 USD | 247.60 USD | 0.00 USD | `+17.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 354,440.00 USD | 74,840.00 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 354,990.00 USD | 544.88 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 357,160.00 USD | 2,170.00 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 358,690.00 USD | 1,540.00 USD | 0.00 USD | `+21.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 368,620.00 USD | 9,930.00 USD | 0.00 USD | `+21.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 369,500.00 USD | 877.63 USD | 0.00 USD | `+23.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 369,670.00 USD | 171.50 USD | 0.00 USD | `+23.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 369,840.00 USD | 171.09 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 372,610.00 USD | 2,770.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 374,650.00 USD | 2,040.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 374,840.00 USD | 188.39 USD | 0.00 USD | `+26.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 377,500.00 USD | 2,670.00 USD | 0.00 USD | `+26.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 377,680.00 USD | 174.23 USD | 0.00 USD | `+26.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 377,850.00 USD | 174.38 USD | 0.00 USD | `+26.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 378,030.00 USD | 174.84 USD | 0.00 USD | `+26.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 378,180.00 USD | 150.90 USD | 0.00 USD | `+27.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 378,330.00 USD | 151.03 USD | 0.00 USD | `+27.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 378,480.00 USD | 151.16 USD | 0.00 USD | `+27.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 378,630.00 USD | 151.29 USD | 0.00 USD | `+27.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 378,780.00 USD | 151.42 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 378,930.00 USD | 151.55 USD | 0.00 USD | `+28.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 379,090.00 USD | 151.69 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 381,130.00 USD | 2,050.00 USD | 0.00 USD | `+29.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 381,240.00 USD | 110.00 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 381,720.00 USD | 475.80 USD | 0.00 USD | `+32.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 382,930.00 USD | 1,210.00 USD | 0.00 USD | `+33.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 425,850.00 USD | 42,930.00 USD | 0.00 USD | `+33.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 427,860.00 USD | 2,000.00 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 429,240.00 USD | 1,380.00 USD | 0.00 USD | `+39.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 429,490.00 USD | 245.41 USD | 0.00 USD | `+42.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 437,880.00 USD | 8,390.00 USD | 0.00 USD | `+43.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 438,300.00 USD | 415.25 USD | 0.00 USD | `+44.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 444,810.00 USD | 6,520.00 USD | 0.00 USD | `+44.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 449,610.00 USD | 4,800.00 USD | 0.00 USD | `+45.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 450,270.00 USD | 655.75 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 450,860.00 USD | 596.43 USD | 0.00 USD | `+48.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 452,680.00 USD | 1,810.00 USD | 0.00 USD | `+49.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 466,560.00 USD | 13,880.00 USD | 0.00 USD | `+49.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 467,810.00 USD | 1,250.00 USD | 0.00 USD | `+50.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 469,880.00 USD | 2,070.00 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 470,020.00 USD | 140.05 USD | 0.00 USD | `+55.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 470,180.00 USD | 160.42 USD | 0.00 USD | `+56.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 470,780.00 USD | 598.33 USD | 0.00 USD | `+56.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 504,950.00 USD | 34,170.00 USD | 0.00 USD | `+59.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 505,830.00 USD | 879.84 USD | 0.00 USD | `+65.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 508,890.00 USD | 3,050.00 USD | 0.00 USD | `+68.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 509,180.00 USD | 297.27 USD | 0.00 USD | `+72.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 517,710.00 USD | 8,530.00 USD | 0.00 USD | `+83.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 517,860.00 USD | 143.99 USD | 0.00 USD | `+85.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 518,040.00 USD | 177.05 USD | 0.00 USD | `+96.87%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `192.47M` | Total OI Tokens: `212,183,628.1 DOT`
  * 1h OI Change: `+1.59%` | 4h OI Change: `-2.15%` | 24h OI Change: `-8.45%`
  * Exchange Breakdown: Binance=`34.63M` | Bybit=`21.24M` | OKX=`10.01M` | Hyperliquid=`5.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-39.60` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0029%` | **USDT OKX** | `-0.0232%` |
| **USDT Bybit** | `0.0079%` | **USDT KuCoin** | `-0.0001%` |
| **USDT MEXC** | `0.0017%` | **USDT BingX** | `0.0063%` |
| **USDT Gate** | `0.0054%` | **USDT Bitget** | `-0.0120%` |
| **CoinM Binance** | `-0.0139%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `45.47%` | `54.53%` | `0.83` | 7,820,000.00 USD |
| `15M` | `Binance` | `50.49%` | `49.51%` | `1.02` | 2,800,000.00 USD |
| `15M` | `OKX` | `45.68%` | `54.32%` | `0.84` | 467,370.00 USD |
| `15M` | `Bybit` | `35.97%` | `64.03%` | `0.56` | 448,520.00 USD |
| `15M` | `KuCoin` | `55.4%` | `44.6%` | `1.24` | 15,380.00 USD |
| `15M` | `Gate` | `41.74%` | `58.26%` | `0.72` | 163,580.00 USD |
| `15M` | `Bitget` | `43.06%` | `56.94%` | `0.76` | 384,690.00 USD |
| `15M` | `BingX` | `14.04%` | `85.96%` | `0.16` | 136,700.00 USD |
| `15M` | `MEXC` | `64.73%` | `35.27%` | `1.84` | 2,990,000.00 USD |
| `15M` | `Bitunix` | `45.71%` | `54.29%` | `0.84` | 210,350.00 USD |
| `15M` | `Hyperliquid` | `30.6%` | `69.4%` | `0.44` | 73,420.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.99%` | `51.01%` | `0.96` | 80,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 15,790.00 USD |
| `15M` | `HTX` | `37.01%` | `62.99%` | `0.59` | 1,550.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `50.18%` | `49.82%` | `1.01` | 20,730.00 USD |
| `15M` | `Aster` | `56.12%` | `43.88%` | `1.28` | 3,330.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `63.94%` | `36.06%` | `1.77` | 6,520.00 USD |
| `15M` | `Whale Positions` | `50.49%` | `49.51%` | `1.02` | 2,800,000.00 USD |
| `15M` | `Global Accounts` | `45.47%` | `54.53%` | `0.83` | 7,820,000.00 USD |
| `1H` | `DOT` | `50.42%` | `49.58%` | `1.02` | 57,050,000.00 USD |
| `1H` | `Binance` | `52.59%` | `47.41%` | `1.11` | 22,440,000.00 USD |
| `1H` | `OKX` | `51.2%` | `48.8%` | `1.05` | 7,460,000.00 USD |
| `1H` | `Bybit` | `52.38%` | `47.62%` | `1.10` | 11,550,000.00 USD |
| `1H` | `KuCoin` | `56%` | `44%` | `1.27` | 1,040,000.00 USD |
| `1H` | `Gate` | `50.49%` | `49.51%` | `1.02` | 3,680,000.00 USD |
| `1H` | `Bitget` | `58.61%` | `41.39%` | `1.42` | 1,860,000.00 USD |
| `1H` | `BingX` | `23.73%` | `76.27%` | `0.31` | 662,260.00 USD |
| `1H` | `MEXC` | `51.18%` | `48.82%` | `1.05` | 958,680.00 USD |
| `1H` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 722,540.00 USD |
| `1H` | `Hyperliquid` | `60.93%` | `39.07%` | `1.56` | 2,180,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.35%` | `48.65%` | `1.06` | 810,760.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `12.47%` | `87.53%` | `0.14` | 2,400,000.00 USD |
| `1H` | `HTX` | `58.81%` | `41.19%` | `1.43` | 139,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `32.62%` | `67.38%` | `0.48` | 901,410.00 USD |
| `1H` | `Aster` | `46.12%` | `53.88%` | `0.86` | 93,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `75.76%` | `24.24%` | `3.13` | 155,950.00 USD |
| `1H` | `Whale Positions` | `52.59%` | `47.41%` | `1.11` | 22,440,000.00 USD |
| `1H` | `Global Accounts` | `50.42%` | `49.58%` | `1.02` | 57,050,000.00 USD |
| `4H` | `DOT` | `50.32%` | `49.68%` | `1.01` | 546,690,000.00 USD |
| `4H` | `Binance` | `50.92%` | `49.08%` | `1.04` | 235,910,000.00 USD |
| `4H` | `OKX` | `51.59%` | `48.41%` | `1.07` | 70,690,000.00 USD |
| `4H` | `Bybit` | `49.44%` | `50.56%` | `0.98` | 104,840,000.00 USD |
| `4H` | `KuCoin` | `50.18%` | `49.82%` | `1.01` | 4,400,000.00 USD |
| `4H` | `Gate` | `49.23%` | `50.77%` | `0.97` | 20,050,000.00 USD |
| `4H` | `Bitget` | `54.79%` | `45.21%` | `1.21` | 15,130,000.00 USD |
| `4H` | `BingX` | `50.96%` | `49.04%` | `1.04` | 5,730,000.00 USD |
| `4H` | `MEXC` | `48.02%` | `51.98%` | `0.92` | 7,430,000.00 USD |
| `4H` | `Bitunix` | `50.2%` | `49.8%` | `1.01` | 8,660,000.00 USD |
| `4H` | `Hyperliquid` | `52.17%` | `47.83%` | `1.09` | 26,260,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.36%` | `49.64%` | `1.01` | 8,720,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `36%` | `64%` | `0.56` | 22,780,000.00 USD |
| `4H` | `HTX` | `54.96%` | `45.04%` | `1.22` | 1,710,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `64.05%` | `35.95%` | `1.78` | 7,500,000.00 USD |
| `4H` | `Aster` | `55.78%` | `44.22%` | `1.26` | 3,240,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.01%` | `54.99%` | `0.82` | 3,620,000.00 USD |
| `4H` | `Whale Positions` | `50.92%` | `49.08%` | `1.04` | 235,910,000.00 USD |
| `4H` | `Global Accounts` | `50.32%` | `49.68%` | `1.01` | 546,690,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.9183` | `0.9184` | `0.9183` | `0.9224` | `0.9157` | 756,618.37 USD | 401,723.78 USD | 354,894.58 USD | 46,829.20 USD | `+6.19%` | `7B / 8S` |
| `5:00 UTC` | `0.9119` | `0.9113` | `0.9119` | `0.9180` | `0.9075` | 1,642,747.02 USD | 649,081.56 USD | 993,665.46 USD | -344,583.90 USD | `-20.98%` | `8B / 21S` |
| `0:00 UTC` | `0.9058` | `0.9071` | `0.9058` | `0.9105` | `0.9032` | 1,657,888.03 USD | 850,360.13 USD | 807,527.90 USD | 42,832.23 USD | `+2.58%` | `4B / 3S` |
| `5:00 UTC` | `0.8801` | `0.8838` | `0.8801` | `0.9093` | `0.8673` | 5,952,763.88 USD | 2,490,126.99 USD | 3,462,636.89 USD | -972,509.89 USD | `-16.34%` | `2B / 19S` |
| `0:00 UTC` | `0.8878` | `0.8837` | `0.8878` | `0.8906` | `0.8749` | 2,004,907.71 USD | 957,094.96 USD | 1,047,812.74 USD | -90,717.78 USD | `-4.52%` | `8B / 10S` |
| `5:00 UTC` | `0.8981` | `0.8950` | `0.8981` | `0.8992` | `0.8880` | 981,791.86 USD | 533,907.73 USD | 447,884.13 USD | 86,023.61 USD | `+8.76%` | `24B / 13S` |
| `0:00 UTC` | `0.9128` | `0.9067` | `0.9128` | `0.9188` | `0.8940` | 5,309,559.22 USD | 3,731,112.91 USD | 1,578,446.31 USD | 2,152,666.61 USD | `+40.54%` | `37B / 0S` |
| `5:00 UTC` | `0.9064` | `0.9085` | `0.9064` | `0.9120` | `0.9046` | 994,017.98 USD | 572,287.48 USD | 421,730.50 USD | 150,556.98 USD | `+15.15%` | `8B / 2S` |
| `0:00 UTC` | `0.9111` | `0.9070` | `0.9111` | `0.9142` | `0.8973` | 1,250,275.83 USD | 633,543.99 USD | 616,731.85 USD | 16,812.14 USD | `+1.34%` | `19B / 16S` |
| `5:00 UTC` | `0.9043` | `0.9050` | `0.9043` | `0.9096` | `0.9016` | 378,467.02 USD | 186,702.56 USD | 191,764.47 USD | -5,061.91 USD | `-1.34%` | `8B / 15S` |

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
| `5m` | -7,420.00 USD | 14,830.00 USD | **`ACCUMULATION`** |
| `15m` | -40,930.00 USD | -58,670.00 USD | **`DISTRIBUTION`** |
| `30m` | -141,060.00 USD | 73,800.00 USD | **`DISTRIBUTION`** |
| `1h` | 37,790.00 USD | 2,810,000.00 USD | **`ACCUMULATION`** |
| `2h` | -384,120.00 USD | 942,400.00 USD | **`ACCUMULATION`** |
| `4h` | -241,540.00 USD | 721,730.00 USD | **`ACCUMULATION`** |
| `6h` | -1,130,000.00 USD | -5,970,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,150,000.00 USD | -6,240,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,210,000.00 USD | -7,390,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,130,000.00 USD | -6,950,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,470,000.00 USD | -25,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,760,000.00 USD | -78,400,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-7.42K` | 15m=`-40.93K` | 1h=`+37.79K` | 24h=`-1.13M`
* Futures Capital Netflows: 5m=`+14.83K` | 15m=`-58.67K` | 1h=`+2.81M` | 24h=`-6.95M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8890` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8414` (Risk Distance: `0.0476` pts)
  * +2.5R Take Profit: `1.01`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9216` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9692` (Risk Distance: `0.0476` pts)
  * +2.5R Take Profit: `0.8027`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9087`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
