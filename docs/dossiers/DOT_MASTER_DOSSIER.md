# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOT
**Canonical Key**: `DOT` | **Broker Instrument**: `DOTUSD.pi` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 08:12:35 IST` (`2026-10-30 02:42:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.8950` | **Live Ask Quote**: `0.9160` | **Mid Price**: `0.9055`
- **Spread Points**: `21.00` | **Spread BPS**: `231.92 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `0.8855` | VWAP Z-Score: `+0.96` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0130` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `38.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.9153` | Lower -3.00σ Band: `0.8557`
  * Upper +2.51σ Band: `0.9104` | Lower -2.51σ Band: `0.8606`
  * Upper +2.01σ Band: `0.9055` | Lower -2.01σ Band: `0.8655`
  * Upper +2.00σ Band: `0.9054` | Lower -2.00σ Band: `0.8656`
  * Upper +1.28σ Band: `0.8982` | Lower -1.28σ Band: `0.8728`
  * Upper +1.00σ Band: `0.8954` | Lower -1.00σ Band: `0.8756`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.8954` | EMA-20=`0.9068` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.9336` (Slope: `+0.0000`) | EMA-100=`0.9531`
  * Institutional Anchors: EMA-144=`0.9612` | EMA-200=`0.9666` (Slope: `-0.9337`) | EMA-233=`0.9705`
- **Range Boundaries**: 24H High=`1.01` | 24H Low=`0.8570` | Weekly High=`1.03` | Weekly Low=`0.8570`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.9216` (Distance: `-1.48%`)
  * Point of Control (POC) = `0.9121` (Distance: `-0.45%`)
  * Value Area Low (VAL) = `0.8899` (Distance: `+2.03%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.9991` | POC=`0.9750` | VAL=`0.9546`
  * Prior Day Extremes: PDH=`1.02` | PDL=`0.8800` | PDC=`0.9000`
  * Monday Range Blueprint: High=`1.03` | Mid=`1.01` | Low=`0.9890`
  * Developing Weekly Value Area: Weekly VAH=`1.01` | Weekly POC=`0.9945` | Weekly VAL=`0.9724`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.9280` | Low=`0.8570`
  * London Session (08:00-16:00 UTC): High=`0.9091` | Low=`0.9019`
  * New York Session (13:00-21:00 UTC): High=`0.9109` | Low=`0.9001`
  * Initial Balance (First Hour): IB High=`0.9082` | IB Low=`0.9028`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.9019` - `0.9091`
  * Optimal Trade Entry (OTE 0.705): `0.9073`
  * Structural Invalidation Anchor (0.786): `0.9127`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.9068` | `0.9087` | `0.9022` | `0.9022` | `726,242` | 656,990.01 USD | -314,583.65 USD | `-47.88%` | -3,845,598.22 USD | `-0.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.9023` | `0.9085` | `0.9022` | `0.9064` | `272,793` | 247,072.82 USD | 22,884.17 USD | `+9.26%` | -3,822,714.05 USD | `-0.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.9065` | `0.9096` | `0.9065` | `0.9091` | `158,773` | 144,229.59 USD | 34,697.26 USD | `+24.06%` | -3,788,016.79 USD | `-0.18` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.9053` | `0.9141` | `0.8973` | `0.9088` | `1,378,655` | 1,250,275.83 USD | 16,812.14 USD | `+1.34%` | -3,536,182.82 USD | `+0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.9088` | `0.9096` | `0.9016` | `0.9068` | `739,056` | 668,740.93 USD | 5,168.25 USD | `+0.77%` | -3,531,014.57 USD | `+0.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.9068` | `0.9096` | `0.9022` | `0.9092` | `1,158,356` | 1,048,790.08 USD | -256,738.95 USD | `-24.48%` | -3,787,753.52 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.9089` | `0.9105` | `0.8671` | `0.8988` | `11,929,789` | 10,597,351.48 USD | -934,371.84 USD | `-8.82%` | -5,948,224.27 USD | `-0.79` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.8988` | `0.9187` | `0.8939` | `0.9068` | `9,068,149` | 8,222,593.96 USD | 2,325,203.98 USD | `+28.28%` | -3,623,020.29 USD | `+2.56` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.9068` | `0.9096` | `0.9022` | `0.9092` | `1,158,356` | 1,048,790.08 USD | -256,738.95 USD | `-24.48%` | -3,879,759.24 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -876,375.92 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,401,104.65 USD | `-1.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9187` | `0.8671` | `0.9090` | `22,155,757` | 19,868,247.68 USD | 1,133,820.11 USD | `+5.71%` | -4,267,284.54 USD | `+1.03` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.9732` | `0.9961` | `0.9713` | `0.9832` | `7,577,906` | 7,454,920.57 USD | 85,064.41 USD | `+1.14%` | 98,266.33 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.9833` | `1.02` | `0.9787` | `1.02` | `11,654,721` | 11,655,736.18 USD | -177,576.81 USD | `-1.52%` | -79,310.47 USD | `-1.36` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.02` | `1.02` | `0.9766` | `0.9844` | `11,576,299` | 11,511,461.28 USD | -797,065.44 USD | `-6.92%` | -876,375.92 USD | `-1.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9845` | `0.9849` | `0.8892` | `0.9088` | `44,360,278` | 41,175,320.93 USD | -4,524,728.73 USD | `-10.99%` | -5,401,104.65 USD | `-1.97` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.9089` | `0.9187` | `0.8671` | `0.9090` | `22,155,757` | 19,868,247.68 USD | 1,133,820.11 USD | `+5.71%` | -4,267,284.54 USD | `+1.03` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

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
| `Live` | `Long Liquidation` | `0.2025` | 101.25 USD | 325,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 2,580.00 USD | 325,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3295` | 110.15 USD | 322,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3735` | 825.06 USD | 322,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4005` | 687.06 USD | 321,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 2,790.00 USD | 320,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 369.92 USD | 318,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 315.16 USD | 317,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4695` | 2,580.00 USD | 317,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 2,770.00 USD | 314,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5065` | 3,290.00 USD | 312,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5645` | 564.50 USD | 308,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5655` | 14,600.00 USD | 308,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5695` | 577.36 USD | 293,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5845` | 683.51 USD | 293,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5895` | 137.53 USD | 292,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5905` | 122.88 USD | 292,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6055` | 2,260.00 USD | 292,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6065` | 1,800.00 USD | 289,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6125` | 105.96 USD | 288,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6145` | 147.48 USD | 287,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6275` | 62,750.00 USD | 287,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6315` | 757.80 USD | 225,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6355` | 106.00 USD | 224,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6405` | 2,090.00 USD | 224,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6415` | 20,270.00 USD | 222,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6465` | 4,230.00 USD | 201,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6475` | 202.47 USD | 197,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6575` | 260.70 USD | 197,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6595` | 149.44 USD | 197,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6775` | 423.10 USD | 196,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6835` | 512.97 USD | 196,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6865` | 68,650.00 USD | 196,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6895` | 276.28 USD | 127,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6965` | 322.62 USD | 127,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6995` | 20,030.00 USD | 126,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7005` | 1,140.00 USD | 106,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7145` | 988.87 USD | 105,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7215` | 1,580.00 USD | 104,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7235` | 397.93 USD | 103,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7285` | 291.18 USD | 102,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7305` | 2,460.00 USD | 102,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7335` | 1,140.00 USD | 99,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7395` | 283.30 USD | 98,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7445` | 52,860.00 USD | 98,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7525` | 331.18 USD | 45,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7535` | 1,400.00 USD | 45,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7555` | 8,990.00 USD | 43,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7725` | 3,840.00 USD | 34,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7795` | 272.83 USD | 31,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7835` | 5,620.00 USD | 30,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7865` | 292.03 USD | 25,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.7890` | 2,090,000.00 USD | 2,090,000.00 USD | 7,140.00 USD | 2,140.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.7905` | 277.39 USD | 24,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.8135` | 647.79 USD | 24,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8150` | 1,840,000.00 USD | 1,840,000.00 USD | 5,990.00 USD | 7,610.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8170` | 1,820,000.00 USD | 1,820,000.00 USD | 10,780.00 USD | 2,370.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8190` | 1,800,000.00 USD | 1,800,000.00 USD | 8,920.00 USD | 2,530.00 USD | 4,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8210` | 1,780,000.00 USD | 1,780,000.00 USD | 7,510.00 USD | 3,060.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8215` | 1,950.00 USD | 23,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8220` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 471.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8230` | 1,760,000.00 USD | 1,760,000.00 USD | 29,430.00 USD | 4,660.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8235` | 749.96 USD | 21,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `0.8365` | 316.70 USD | 21,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.8370` | 1,640,000.00 USD | 1,640,000.00 USD | 15,240.00 USD | 154.74 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8380` | 1,370,000.00 USD | 1,370,000.00 USD | 9,580.00 USD | 1,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8390` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 798.38 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.8400` | 1,360,000.00 USD | 1,360,000.00 USD | 458.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8410` | 1,620,000.00 USD | 1,620,000.00 USD | 270.00 USD | 804.10 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8415` | 1,570.00 USD | 20,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8420` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 149.63 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8430` | 1,610,000.00 USD | 1,610,000.00 USD | 6,590.00 USD | 3,620.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8435` | 143.90 USD | 19,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8440` | 1,360,000.00 USD | 1,360,000.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8450` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 474.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8470` | 1,600,000.00 USD | 1,600,000.00 USD | 7,900.00 USD | 1,130.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8490` | 1,590,000.00 USD | 1,590,000.00 USD | 731.45 USD | 132.08 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8495` | 1,260.00 USD | 19,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8500` | 1,350,000.00 USD | 1,350,000.00 USD | 421.90 USD | 61.55 USD | 206.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8510` | 1,590,000.00 USD | 1,590,000.00 USD | 5,480.00 USD | 114.10 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.8515` | 2,700.00 USD | 17,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.8520` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,940.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.8530` | 1,580,000.00 USD | 1,580,000.00 USD | 2,130.00 USD | 2,670.00 USD | 1,160.00 USD | `Tier 1 CEX` |
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
| `Live` | `Short Liquidation` | `0.9695` | 9,870.00 USD | 9,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9700` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 2,090.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9710` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 13,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9720` | 1,680,000.00 USD | 1,680,000.00 USD | 24,360.00 USD | 174.50 USD | 23,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9730` | 2,180,000.00 USD | 2,180,000.00 USD | 2,910.00 USD | 9,050.00 USD | 7,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9735` | 213.78 USD | 10,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9740` | 1,730,000.00 USD | 1,730,000.00 USD | 25,800.00 USD | 5,170.00 USD | 14,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9750` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 16,590.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9760` | 1,810,000.00 USD | 1,810,000.00 USD | 53,340.00 USD | 13,960.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9770` | 2,300,000.00 USD | 2,300,000.00 USD | 49,900.00 USD | 16,230.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9780` | 1,870,000.00 USD | 1,870,000.00 USD | 39,980.00 USD | 3,080.00 USD | 17,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9785` | 216.54 USD | 10,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9790` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 84,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9795` | 216.76 USD | 10,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9800` | 1,930,000.00 USD | 1,930,000.00 USD | 29,240.00 USD | 9,580.00 USD | 20,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9810` | 2,510,000.00 USD | 2,510,000.00 USD | 540.00 USD | 0.00 USD | 118,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9820` | 1,960,000.00 USD | 1,960,000.00 USD | 16,350.00 USD | 12,360.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9830` | 2,680,000.00 USD | 2,680,000.00 USD | 102,710.00 USD | 15,810.00 USD | 52,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9840` | 2,010,000.00 USD | 2,010,000.00 USD | 665.59 USD | 13,370.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9850` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 1,000.00 USD | 22,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9855` | 217.40 USD | 10,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.9860` | 2,090,000.00 USD | 2,090,000.00 USD | 50,550.00 USD | 3,510.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9870` | 2,800,000.00 USD | 2,800,000.00 USD | 40,020.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9880` | 2,120,000.00 USD | 2,120,000.00 USD | 17,200.00 USD | 130.81 USD | 14,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9890` | 2,820,000.00 USD | 2,820,000.00 USD | 20,530.00 USD | 284.26 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9900` | 2,190,000.00 USD | 2,190,000.00 USD | 57,390.00 USD | 1,300.00 USD | 13,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9905` | 218.50 USD | 10,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9910` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 19,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9920` | 2,220,000.00 USD | 2,220,000.00 USD | 9,210.00 USD | 2,900.00 USD | 13,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9930` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9940` | 2,240,000.00 USD | 2,240,000.00 USD | 12,310.00 USD | 13,250.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9950` | 2,920,000.00 USD | 2,920,000.00 USD | 33,790.00 USD | 5,380.00 USD | 42,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9960` | 2,270,000.00 USD | 2,270,000.00 USD | 18,530.00 USD | 4,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.9970` | 3,000,000.00 USD | 3,000,000.00 USD | 69,270.00 USD | 0.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.9980` | 2,320,000.00 USD | 2,320,000.00 USD | 40,410.00 USD | 4,790.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.9985` | 220.27 USD | 11,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.9990` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 104.05 USD | 462.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 59,960.00 USD | 27,710.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,050,000.00 USD | 3,050,000.00 USD | 52,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,410,000.00 USD | 2,410,000.00 USD | 501.30 USD | 0.00 USD | 266.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,200,000.00 USD | 3,200,000.00 USD | 105,770.00 USD | 21,740.00 USD | 16,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.00` | 2,440,000.00 USD | 2,440,000.00 USD | 10,110.00 USD | 9,540.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.00` | 3,230,000.00 USD | 3,230,000.00 USD | 32,430.00 USD | 3,970.00 USD | 1,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.01` | 2,580,000.00 USD | 2,580,000.00 USD | 101,040.00 USD | 10,140.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.01` | 221.13 USD | 11,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.04` | 228.37 USD | 11,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,030,000.00 USD | 6,030,000.00 USD | 239,580.00 USD | 8,210.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,470,000.00 USD | 6,470,000.00 USD | 276,890.00 USD | 1,800.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,660,000.00 USD | 6,660,000.00 USD | 49,280.00 USD | 32,550.00 USD | 114,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.04` | 6,930,000.00 USD | 6,930,000.00 USD | 184,670.00 USD | 23,680.00 USD | 59,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.05` | 7,450,000.00 USD | 7,450,000.00 USD | 178,890.00 USD | 96,750.00 USD | 238,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.05` | 367.04 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.08` | 2,230.00 USD | 14,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.11` | 169.86 USD | 14,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Short Liquidation` | `1.15` | 117.41 USD | 14,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 2,450.00 USD | 16,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 22,180.00 USD | 39,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.32` | 11,730.00 USD | 50,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.34` | 239.77 USD | 51,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,190.00 USD | 54,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 176.31 USD | 54,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,810.00 USD | 56,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 795.29 USD | 57,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 2,440.00 USD | 59,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.63` | 129.55 USD | 59,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 8,240.00 USD | 67,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 243.52 USD | 68,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 300.15 USD | 68,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 326.71 USD | 68,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 190.42 USD | 68,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 132.74 USD | 69,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2025` | 325,230.00 USD | 0.00 USD | 101.25 USD | `-77.68%` | `500.00` |
| `Live` | `Long` | `0.2815` | 325,130.00 USD | 0.00 USD | 2,580.00 USD | `-68.97%` | `9,174.90` |
| `Live` | `Long` | `0.3295` | 322,550.00 USD | 0.00 USD | 110.15 USD | `-63.68%` | `334.30` |
| `Live` | `Long` | `0.3735` | 322,440.00 USD | 0.00 USD | 825.06 USD | `-58.82%` | `2,209.00` |
| `Live` | `Long` | `0.4005` | 321,610.00 USD | 0.00 USD | 687.06 USD | `-55.85%` | `1,715.50` |
| `Live` | `Long` | `0.4185` | 320,920.00 USD | 0.00 USD | 2,790.00 USD | `-53.86%` | `6,675.20` |
| `Live` | `Long` | `0.4535` | 318,130.00 USD | 0.00 USD | 369.92 USD | `-50.00%` | `815.70` |
| `Live` | `Long` | `0.4645` | 317,760.00 USD | 0.00 USD | 315.16 USD | `-48.79%` | `678.50` |
| `Live` | `Long` | `0.4695` | 317,440.00 USD | 0.00 USD | 2,580.00 USD | `-48.24%` | `5,500.00` |
| `Live` | `Long` | `0.4865` | 314,860.00 USD | 0.00 USD | 2,770.00 USD | `-46.37%` | `5,698.80` |
| `Live` | `Long` | `0.5065` | 312,090.00 USD | 0.00 USD | 3,290.00 USD | `-44.16%` | `6,504.70` |
| `Live` | `Long` | `0.5645` | 308,800.00 USD | 0.00 USD | 564.50 USD | `-37.77%` | `1,000.00` |
| `Live` | `Long` | `0.5655` | 308,230.00 USD | 0.00 USD | 14,600.00 USD | `-37.66%` | `25,816.60` |
| `Live` | `Long` | `0.5695` | 293,630.00 USD | 0.00 USD | 577.36 USD | `-37.22%` | `1,013.80` |
| `Live` | `Long` | `0.5845` | 293,050.00 USD | 0.00 USD | 683.51 USD | `-35.56%` | `1,169.40` |
| `Live` | `Long` | `0.5895` | 292,370.00 USD | 0.00 USD | 137.53 USD | `-35.01%` | `233.30` |
| `Live` | `Long` | `0.5905` | 292,230.00 USD | 0.00 USD | 122.88 USD | `-34.90%` | `208.10` |
| `Live` | `Long` | `0.6055` | 292,110.00 USD | 0.00 USD | 2,260.00 USD | `-33.25%` | `3,731.20` |
| `Live` | `Long` | `0.6065` | 289,850.00 USD | 0.00 USD | 1,800.00 USD | `-33.14%` | `2,971.80` |
| `Live` | `Long` | `0.6125` | 288,050.00 USD | 0.00 USD | 105.96 USD | `-32.48%` | `173.00` |
| `Live` | `Long` | `0.6145` | 287,940.00 USD | 0.00 USD | 147.48 USD | `-32.26%` | `240.00` |
| `Live` | `Long` | `0.6275` | 287,800.00 USD | 0.00 USD | 62,750.00 USD | `-30.82%` | `100,000.00` |
| `Live` | `Long` | `0.6315` | 225,050.00 USD | 0.00 USD | 757.80 USD | `-30.38%` | `1,200.00` |
| `Live` | `Long` | `0.6355` | 224,290.00 USD | 0.00 USD | 106.00 USD | `-29.94%` | `166.80` |
| `Live` | `Long` | `0.6405` | 224,180.00 USD | 0.00 USD | 2,090.00 USD | `-29.39%` | `3,262.00` |
| `Live` | `Long` | `0.6415` | 222,090.00 USD | 0.00 USD | 20,270.00 USD | `-29.28%` | `31,595.60` |
| `Live` | `Long` | `0.6465` | 201,820.00 USD | 0.00 USD | 4,230.00 USD | `-28.73%` | `6,539.70` |
| `Live` | `Long` | `0.6475` | 197,600.00 USD | 0.00 USD | 202.47 USD | `-28.62%` | `312.70` |
| `Live` | `Long` | `0.6575` | 197,390.00 USD | 0.00 USD | 260.70 USD | `-27.52%` | `396.50` |
| `Live` | `Long` | `0.6595` | 197,130.00 USD | 0.00 USD | 149.44 USD | `-27.29%` | `226.60` |
| `Live` | `Long` | `0.6775` | 196,980.00 USD | 0.00 USD | 423.10 USD | `-25.31%` | `624.50` |
| `Live` | `Long` | `0.6835` | 196,560.00 USD | 0.00 USD | 512.97 USD | `-24.65%` | `750.50` |
| `Live` | `Long` | `0.6865` | 196,050.00 USD | 0.00 USD | 68,650.00 USD | `-24.32%` | `100,000.00` |
| `Live` | `Long` | `0.6895` | 127,400.00 USD | 0.00 USD | 276.28 USD | `-23.99%` | `400.70` |
| `Live` | `Long` | `0.6965` | 127,120.00 USD | 0.00 USD | 322.62 USD | `-23.22%` | `463.20` |
| `Live` | `Long` | `0.6995` | 126,800.00 USD | 0.00 USD | 20,030.00 USD | `-22.89%` | `28,635.00` |
| `Live` | `Long` | `0.7005` | 106,770.00 USD | 0.00 USD | 1,140.00 USD | `-22.78%` | `1,634.20` |
| `Live` | `Long` | `0.7145` | 105,620.00 USD | 0.00 USD | 988.87 USD | `-21.23%` | `1,384.00` |
| `Live` | `Long` | `0.7215` | 104,630.00 USD | 0.00 USD | 1,580.00 USD | `-20.46%` | `2,190.90` |
| `Live` | `Long` | `0.7235` | 103,050.00 USD | 0.00 USD | 397.93 USD | `-20.24%` | `550.00` |
| `Live` | `Long` | `0.7285` | 102,660.00 USD | 0.00 USD | 291.18 USD | `-19.69%` | `399.70` |
| `Live` | `Long` | `0.7305` | 102,360.00 USD | 0.00 USD | 2,460.00 USD | `-19.47%` | `3,366.40` |
| `Live` | `Long` | `0.7335` | 99,910.00 USD | 0.00 USD | 1,140.00 USD | `-19.14%` | `1,557.80` |
| `Live` | `Long` | `0.7395` | 98,760.00 USD | 0.00 USD | 283.30 USD | `-18.48%` | `383.10` |
| `Live` | `Long` | `0.7445` | 98,480.00 USD | 0.00 USD | 52,860.00 USD | `-17.92%` | `71,003.30` |
| `Live` | `Long` | `0.7525` | 45,620.00 USD | 0.00 USD | 331.18 USD | `-17.04%` | `440.10` |
| `Live` | `Long` | `0.7535` | 45,290.00 USD | 0.00 USD | 1,400.00 USD | `-16.93%` | `1,859.90` |
| `Live` | `Long` | `0.7555` | 43,880.00 USD | 0.00 USD | 8,990.00 USD | `-16.71%` | `11,902.80` |
| `Live` | `Long` | `0.7725` | 34,890.00 USD | 0.00 USD | 3,840.00 USD | `-14.84%` | `4,968.90` |
| `Live` | `Long` | `0.7795` | 31,050.00 USD | 0.00 USD | 272.83 USD | `-14.07%` | `350.00` |
| `Live` | `Long` | `0.7835` | 30,780.00 USD | 0.00 USD | 5,620.00 USD | `-13.62%` | `7,176.90` |
| `Live` | `Long` | `0.7865` | 25,160.00 USD | 0.00 USD | 292.03 USD | `-13.29%` | `371.30` |
| `Live` | `Long` | `0.7905` | 24,870.00 USD | 0.00 USD | 277.39 USD | `-12.85%` | `350.90` |
| `Live` | `Long` | `0.8135` | 24,590.00 USD | 0.00 USD | 647.79 USD | `-10.32%` | `796.30` |
| `Live` | `Long` | `0.8215` | 23,940.00 USD | 0.00 USD | 1,950.00 USD | `-9.44%` | `2,370.70` |
| `Live` | `Long` | `0.8235` | 21,990.00 USD | 0.00 USD | 749.96 USD | `-9.22%` | `910.70` |
| `Live` | `Long` | `0.8365` | 21,240.00 USD | 0.00 USD | 316.70 USD | `-7.78%` | `378.60` |
| `Live` | `Long` | `0.8415` | 20,930.00 USD | 0.00 USD | 1,570.00 USD | `-7.23%` | `1,862.40` |
| `Live` | `Long` | `0.8435` | 19,360.00 USD | 0.00 USD | 143.90 USD | `-7.01%` | `170.60` |
| `Live` | `Long` | `0.8495` | 19,220.00 USD | 0.00 USD | 1,260.00 USD | `-6.35%` | `1,486.90` |
| `Live` | `Long` | `0.8515` | 17,950.00 USD | 0.00 USD | 2,700.00 USD | `-6.13%` | `3,175.90` |
| `Live` | `Long` | `0.8575` | 15,250.00 USD | 0.00 USD | 620.32 USD | `-5.47%` | `723.40` |
| `Live` | `Long` | `0.8635` | 14,630.00 USD | 0.00 USD | 208.02 USD | `-4.81%` | `240.90` |
| `Live` | `Long` | `0.8645` | 14,420.00 USD | 0.00 USD | 438.30 USD | `-4.70%` | `507.00` |
| `Live` | `Long` | `0.8665` | 13,980.00 USD | 0.00 USD | 1,390.00 USD | `-4.47%` | `1,606.10` |
| `Live` | `Long` | `0.8695` | 12,590.00 USD | 0.00 USD | 12,590.00 USD | `-4.14%` | `14,478.80` |
| `Live` | `Short` | `0.9695` | 9,870.00 USD | 9,870.00 USD | 0.00 USD | `+6.88%` | `10,181.70` |
| `Live` | `Short` | `0.9735` | 10,080.00 USD | 213.78 USD | 0.00 USD | `+7.32%` | `219.60` |
| `Live` | `Short` | `0.9785` | 10,300.00 USD | 216.54 USD | 0.00 USD | `+7.87%` | `221.30` |
| `Live` | `Short` | `0.9795` | 10,520.00 USD | 216.76 USD | 0.00 USD | `+7.98%` | `221.30` |
| `Live` | `Short` | `0.9855` | 10,740.00 USD | 217.40 USD | 0.00 USD | `+8.64%` | `220.60` |
| `Live` | `Short` | `0.9905` | 10,950.00 USD | 218.50 USD | 0.00 USD | `+9.20%` | `220.60` |
| `Live` | `Short` | `0.9985` | 11,170.00 USD | 220.27 USD | 0.00 USD | `+10.08%` | `220.60` |
| `Live` | `Short` | `1.01` | 11,400.00 USD | 221.13 USD | 0.00 USD | `+10.96%` | `219.70` |
| `Live` | `Short` | `1.04` | 11,620.00 USD | 228.37 USD | 0.00 USD | `+14.49%` | `219.90` |
| `Live` | `Short` | `1.05` | 11,990.00 USD | 367.04 USD | 0.00 USD | `+15.48%` | `350.40` |
| `Live` | `Short` | `1.08` | 14,220.00 USD | 2,230.00 USD | 0.00 USD | `+19.23%` | `2,064.20` |
| `Live` | `Short` | `1.11` | 14,390.00 USD | 169.86 USD | 0.00 USD | `+22.31%` | `153.10` |
| `Live` | `Short` | `1.15` | 14,510.00 USD | 117.41 USD | 0.00 USD | `+27.28%` | `101.70` |
| `Live` | `Short` | `1.17` | 16,960.00 USD | 2,450.00 USD | 0.00 USD | `+29.04%` | `2,096.60` |
| `Live` | `Short` | `1.19` | 39,150.00 USD | 22,180.00 USD | 0.00 USD | `+31.02%` | `18,664.00` |
| `Live` | `Short` | `1.32` | 50,880.00 USD | 11,730.00 USD | 0.00 USD | `+45.91%` | `8,862.90` |
| `Live` | `Short` | `1.34` | 51,120.00 USD | 239.77 USD | 0.00 USD | `+47.67%` | `179.00` |
| `Live` | `Short` | `1.42` | 54,310.00 USD | 3,190.00 USD | 0.00 USD | `+56.49%` | `2,249.30` |
| `Live` | `Short` | `1.54` | 54,490.00 USD | 176.31 USD | 0.00 USD | `+70.05%` | `114.30` |
| `Live` | `Short` | `1.56` | 56,290.00 USD | 1,810.00 USD | 0.00 USD | `+71.59%` | `1,161.90` |
| `Live` | `Short` | `1.59` | 57,090.00 USD | 795.29 USD | 0.00 USD | `+75.56%` | `499.40` |
| `Live` | `Short` | `1.62` | 59,530.00 USD | 2,440.00 USD | 0.00 USD | `+79.09%` | `1,500.00` |
| `Live` | `Short` | `1.63` | 59,660.00 USD | 129.55 USD | 0.00 USD | `+79.64%` | `79.50` |
| `Live` | `Short` | `1.65` | 67,890.00 USD | 8,240.00 USD | 0.00 USD | `+81.62%` | `5,000.00` |
| `Live` | `Short` | `1.66` | 68,140.00 USD | 243.52 USD | 0.00 USD | `+83.50%` | `146.30` |
| `Live` | `Short` | `1.67` | 68,440.00 USD | 300.15 USD | 0.00 USD | `+83.83%` | `180.00` |
| `Live` | `Short` | `1.70` | 68,760.00 USD | 326.71 USD | 0.00 USD | `+87.69%` | `191.90` |
| `Live` | `Short` | `1.73` | 68,950.00 USD | 190.42 USD | 0.00 USD | `+90.66%` | `110.10` |
| `Live` | `Short` | `1.81` | 69,090.00 USD | 132.74 USD | 0.00 USD | `+99.37%` | `73.40` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.4015` | 334,280.00 USD | 0.00 USD | 120.45 USD | `-55.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 334,160.00 USD | 0.00 USD | 150.15 USD | `-44.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5435` | 334,010.00 USD | 0.00 USD | 186.15 USD | `-40.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6535` | 333,830.00 USD | 0.00 USD | 1,150.00 USD | `-27.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7005` | 332,680.00 USD | 0.00 USD | 781.90 USD | `-22.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7105` | 331,900.00 USD | 0.00 USD | 477.38 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7195` | 331,420.00 USD | 0.00 USD | 341.33 USD | `-20.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7205` | 331,080.00 USD | 0.00 USD | 972.82 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7305` | 330,110.00 USD | 0.00 USD | 160.20 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7385` | 329,940.00 USD | 0.00 USD | 102.58 USD | `-18.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7465` | 329,840.00 USD | 0.00 USD | 289.49 USD | `-17.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7615` | 329,550.00 USD | 0.00 USD | 197.53 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7805` | 329,360.00 USD | 0.00 USD | 14,570.00 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7965` | 314,790.00 USD | 0.00 USD | 274,830.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8005` | 39,950.00 USD | 0.00 USD | 108.47 USD | `-11.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8115` | 39,850.00 USD | 0.00 USD | 405.75 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8365` | 39,440.00 USD | 0.00 USD | 772.84 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8415` | 38,670.00 USD | 0.00 USD | 2,670.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8495` | 36,000.00 USD | 0.00 USD | 3,470.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8505` | 32,530.00 USD | 0.00 USD | 9,180.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8555` | 23,350.00 USD | 0.00 USD | 341.94 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8565` | 23,000.00 USD | 0.00 USD | 1,150.00 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8585` | 21,860.00 USD | 0.00 USD | 429.25 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8605` | 21,430.00 USD | 0.00 USD | 223.30 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8665` | 21,200.00 USD | 0.00 USD | 518.51 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8725` | 20,690.00 USD | 0.00 USD | 649.66 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8825` | 20,040.00 USD | 0.00 USD | 194.06 USD | `-2.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8845` | 19,840.00 USD | 0.00 USD | 193.35 USD | `-2.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8865` | 19,650.00 USD | 0.00 USD | 223.04 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8875` | 19,430.00 USD | 0.00 USD | 10,840.00 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8895` | 8,580.00 USD | 0.00 USD | 4,920.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8915` | 3,660.00 USD | 0.00 USD | 195.86 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8925` | 3,470.00 USD | 0.00 USD | 192.07 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8935` | 3,280.00 USD | 0.00 USD | 195.32 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8965` | 3,080.00 USD | 0.00 USD | 196.87 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8985` | 2,880.00 USD | 0.00 USD | 198.21 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9005` | 2,690.00 USD | 0.00 USD | 1,590.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9025` | 1,090.00 USD | 0.00 USD | 398.91 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9035` | 695.96 USD | 0.00 USD | 196.96 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9045` | 499.00 USD | 0.00 USD | 300.38 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9065` | 198.61 USD | 0.00 USD | 198.61 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9075` | 994.35 USD | 994.35 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 1,360.00 USD | 363.40 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9095` | 1,760.00 USD | 398.72 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9115` | 1,960.00 USD | 199.80 USD | 0.00 USD | `+0.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9135` | 2,160.00 USD | 201.52 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9155` | 2,560.00 USD | 403.92 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9165` | 2,760.00 USD | 198.06 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9175` | 3,160.00 USD | 396.82 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9185` | 4,060.00 USD | 899.85 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9195` | 4,960.00 USD | 900.19 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9205` | 5,360.00 USD | 407.41 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9215` | 5,770.00 USD | 407.30 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9225` | 5,970.00 USD | 201.94 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9255` | 6,790.00 USD | 817.40 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9275` | 8,910.00 USD | 2,120.00 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9285` | 9,150.00 USD | 246.05 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9295` | 9,560.00 USD | 407.49 USD | 0.00 USD | `+2.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9305` | 9,770.00 USD | 203.97 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9325` | 10,010.00 USD | 241.98 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9335` | 10,210.00 USD | 201.64 USD | 0.00 USD | `+2.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9355` | 10,410.00 USD | 201.97 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 20,100.00 USD | 9,680.00 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9395` | 20,510.00 USD | 416.01 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 21,070.00 USD | 555.18 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9425` | 21,880.00 USD | 816.96 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9445` | 23,610.00 USD | 1,730.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9455` | 23,990.00 USD | 383.87 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9465` | 24,620.00 USD | 623.93 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9485` | 25,030.00 USD | 414.68 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9525` | 25,410.00 USD | 381.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9535` | 27,430.00 USD | 2,020.00 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9555` | 27,640.00 USD | 206.77 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9565` | 27,880.00 USD | 236.26 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9575` | 28,010.00 USD | 136.83 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9605` | 28,390.00 USD | 376.80 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9625` | 30,290.00 USD | 1,910.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9635` | 30,860.00 USD | 568.75 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9645` | 31,030.00 USD | 163.29 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9675` | 31,410.00 USD | 385.74 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9695` | 33,450.00 USD | 2,030.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9705` | 33,710.00 USD | 262.52 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9725` | 34,100.00 USD | 387.83 USD | 0.00 USD | `+7.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9735` | 41,730.00 USD | 7,630.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9745` | 50,470.00 USD | 8,750.00 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9755` | 72,440.00 USD | 21,960.00 USD | 0.00 USD | `+7.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9765` | 72,830.00 USD | 396.17 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9775` | 73,510.00 USD | 676.53 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9805` | 81,860.00 USD | 8,350.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9815` | 83,890.00 USD | 2,030.00 USD | 0.00 USD | `+8.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9825` | 85,950.00 USD | 2,060.00 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9845` | 86,200.00 USD | 255.38 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9855` | 101,280.00 USD | 15,070.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9865` | 101,390.00 USD | 109.99 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9895` | 136,360.00 USD | 34,970.00 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9915` | 139,880.00 USD | 3,520.00 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9925` | 171,630.00 USD | 31,750.00 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9935` | 172,040.00 USD | 403.06 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9955` | 172,440.00 USD | 403.28 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9975` | 177,580.00 USD | 5,140.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9985` | 214,890.00 USD | 37,310.00 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 215,890.00 USD | 1,000.00 USD | 0.00 USD | `+10.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 256,490.00 USD | 40,590.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 256,720.00 USD | 235.79 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 258,070.00 USD | 1,340.00 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 258,300.00 USD | 230.39 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 258,510.00 USD | 218.64 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 258,920.00 USD | 409.86 USD | 0.00 USD | `+11.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 259,030.00 USD | 110.95 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.01` | 259,650.00 USD | 615.60 USD | 0.00 USD | `+11.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 260,210.00 USD | 561.17 USD | 0.00 USD | `+11.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.02` | 260,310.00 USD | 103.07 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 260,520.00 USD | 207.97 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 260,730.00 USD | 208.26 USD | 0.00 USD | `+13.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 261,250.00 USD | 516.75 USD | 0.00 USD | `+13.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 261,600.00 USD | 348.86 USD | 0.00 USD | `+14.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 261,990.00 USD | 391.80 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 262,400.00 USD | 413.76 USD | 0.00 USD | `+14.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 262,760.00 USD | 354.91 USD | 0.00 USD | `+14.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 264,660.00 USD | 1,900.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 264,870.00 USD | 207.87 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.04` | 265,080.00 USD | 207.97 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 265,180.00 USD | 107.99 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 340,020.00 USD | 74,840.00 USD | 0.00 USD | `+17.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.07` | 340,570.00 USD | 544.88 USD | 0.00 USD | `+18.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 342,740.00 USD | 2,170.00 USD | 0.00 USD | `+20.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.09` | 344,270.00 USD | 1,540.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 354,200.00 USD | 9,930.00 USD | 0.00 USD | `+20.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.11` | 355,080.00 USD | 877.63 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 355,250.00 USD | 171.09 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.12` | 358,020.00 USD | 2,770.00 USD | 0.00 USD | `+23.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 360,060.00 USD | 2,040.00 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 360,250.00 USD | 187.72 USD | 0.00 USD | `+24.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.13` | 360,430.00 USD | 188.39 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 363,100.00 USD | 2,670.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 363,270.00 USD | 174.23 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 363,450.00 USD | 174.38 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.14` | 363,620.00 USD | 174.84 USD | 0.00 USD | `+25.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 363,770.00 USD | 150.90 USD | 0.00 USD | `+26.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 363,920.00 USD | 151.03 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 364,080.00 USD | 151.16 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 364,230.00 USD | 151.29 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 364,380.00 USD | 151.42 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.15` | 364,530.00 USD | 151.55 USD | 0.00 USD | `+27.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 366,580.00 USD | 2,050.00 USD | 0.00 USD | `+28.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.17` | 366,690.00 USD | 110.00 USD | 0.00 USD | `+29.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.19` | 367,160.00 USD | 475.80 USD | 0.00 USD | `+31.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 368,370.00 USD | 1,210.00 USD | 0.00 USD | `+32.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.20` | 411,300.00 USD | 42,930.00 USD | 0.00 USD | `+32.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 413,300.00 USD | 2,000.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 414,690.00 USD | 1,380.00 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 414,930.00 USD | 245.41 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 423,330.00 USD | 8,390.00 USD | 0.00 USD | `+42.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 423,740.00 USD | 415.25 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 430,260.00 USD | 6,520.00 USD | 0.00 USD | `+43.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 435,050.00 USD | 4,800.00 USD | 0.00 USD | `+44.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 435,710.00 USD | 655.75 USD | 0.00 USD | `+44.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 436,310.00 USD | 596.43 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 438,120.00 USD | 1,810.00 USD | 0.00 USD | `+47.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 452,000.00 USD | 13,880.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 453,260.00 USD | 1,250.00 USD | 0.00 USD | `+49.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 455,330.00 USD | 2,070.00 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 455,470.00 USD | 140.05 USD | 0.00 USD | `+54.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 455,630.00 USD | 160.42 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 456,580.00 USD | 954.32 USD | 0.00 USD | `+55.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 490,750.00 USD | 34,170.00 USD | 0.00 USD | `+58.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 491,630.00 USD | 879.84 USD | 0.00 USD | `+64.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 494,690.00 USD | 3,050.00 USD | 0.00 USD | `+67.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 494,980.00 USD | 297.27 USD | 0.00 USD | `+71.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 503,510.00 USD | 8,530.00 USD | 0.00 USD | `+82.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 503,660.00 USD | 143.99 USD | 0.00 USD | `+83.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 503,840.00 USD | 177.05 USD | 0.00 USD | `+95.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 504,270.00 USD | 431.40 USD | 0.00 USD | `+98.49%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `196.03M` | Total OI Tokens: `212,794,651.4 DOT`
  * 1h OI Change: `+2.62%` | 4h OI Change: `-1.34%` | 24h OI Change: `-6.38%`
  * Exchange Breakdown: Binance=`35.54M` | Bybit=`21.85M` | OKX=`10.26M` | Hyperliquid=`5.53M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.94K` | Last 24h: `2.25K` | Last 3d: `-11.45K` | Last 7d: `-19.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0063%` | **USDT OKX** | `-0.0239%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0017%` |
| **USDT MEXC** | `0.0061%` | **USDT BingX** | `0.0096%` |
| **USDT Gate** | `0.0091%` | **USDT Bitget** | `-0.0085%` |
| **CoinM Binance** | `-0.0130%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOT` | `59.75%` | `40.25%` | `1.48` | 8,730,000.00 USD |
| `15M` | `Binance` | `56.85%` | `43.15%` | `1.32` | 3,430,000.00 USD |
| `15M` | `OKX` | `62.56%` | `37.44%` | `1.67` | 1,390,000.00 USD |
| `15M` | `Bybit` | `56.6%` | `43.4%` | `1.30` | 1,020,000.00 USD |
| `15M` | `KuCoin` | `70.88%` | `29.12%` | `2.43` | 103,050.00 USD |
| `15M` | `Gate` | `69.93%` | `30.07%` | `2.33` | 338,920.00 USD |
| `15M` | `Bitget` | `42.98%` | `57.02%` | `0.75` | 790,780.00 USD |
| `15M` | `BingX` | `77.86%` | `22.14%` | `3.52` | 286,830.00 USD |
| `15M` | `MEXC` | `66.96%` | `33.04%` | `2.03` | 613,920.00 USD |
| `15M` | `Bitunix` | `49.62%` | `50.38%` | `0.98` | 263,490.00 USD |
| `15M` | `Hyperliquid` | `68.26%` | `31.74%` | `2.15` | 147,460.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `68.91%` | `31.09%` | `2.22` | 38,090.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 198,090.00 USD |
| `15M` | `HTX` | `68.64%` | `31.36%` | `2.19` | 8,540.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `14.21%` | `85.79%` | `0.17` | 11,740.00 USD |
| `15M` | `Aster` | `85.44%` | `14.56%` | `5.87` | 76,990.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `47.61%` | `52.39%` | `0.91` | 4,850.00 USD |
| `15M` | `Whale Positions` | `56.85%` | `43.15%` | `1.32` | 3,430,000.00 USD |
| `15M` | `Global Accounts` | `59.75%` | `40.25%` | `1.48` | 8,730,000.00 USD |
| `1H` | `DOT` | `51.73%` | `48.27%` | `1.07` | 9,610,000.00 USD |
| `1H` | `Binance` | `49.64%` | `50.36%` | `0.99` | 3,690,000.00 USD |
| `1H` | `OKX` | `55.84%` | `44.16%` | `1.26` | 1,160,000.00 USD |
| `1H` | `Bybit` | `57.41%` | `42.59%` | `1.35` | 999,350.00 USD |
| `1H` | `KuCoin` | `51.75%` | `48.25%` | `1.07` | 556,850.00 USD |
| `1H` | `Gate` | `47.78%` | `52.22%` | `0.91` | 329,490.00 USD |
| `1H` | `Bitget` | `41.84%` | `58.16%` | `0.72` | 242,740.00 USD |
| `1H` | `BingX` | `39.15%` | `60.85%` | `0.64` | 534,810.00 USD |
| `1H` | `MEXC` | `48.51%` | `51.49%` | `0.94` | 559,220.00 USD |
| `1H` | `Bitunix` | `46.78%` | `53.22%` | `0.88` | 255,510.00 USD |
| `1H` | `Hyperliquid` | `71%` | `29%` | `2.45` | 155,630.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.1%` | `50.9%` | `0.96` | 800,020.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 245,560.00 USD |
| `1H` | `HTX` | `37.18%` | `62.82%` | `0.59` | 10,120.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.4%` | `64.6%` | `0.55` | 50,440.00 USD |
| `1H` | `Aster` | `4.66%` | `95.34%` | `0.05` | 22,770.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `49.64%` | `50.36%` | `0.99` | 3,690,000.00 USD |
| `1H` | `Global Accounts` | `51.73%` | `48.27%` | `1.07` | 9,610,000.00 USD |
| `4H` | `DOT` | `51.33%` | `48.67%` | `1.05` | 574,060,000.00 USD |
| `4H` | `Binance` | `51.76%` | `48.24%` | `1.07` | 226,820,000.00 USD |
| `4H` | `OKX` | `50.98%` | `49.02%` | `1.04` | 65,810,000.00 USD |
| `4H` | `Bybit` | `47.59%` | `52.41%` | `0.91` | 75,950,000.00 USD |
| `4H` | `KuCoin` | `46.91%` | `53.09%` | `0.88` | 4,070,000.00 USD |
| `4H` | `Gate` | `55.28%` | `44.72%` | `1.24` | 16,640,000.00 USD |
| `4H` | `Bitget` | `44.15%` | `55.85%` | `0.79` | 25,840,000.00 USD |
| `4H` | `BingX` | `37.81%` | `62.19%` | `0.61` | 20,020,000.00 USD |
| `4H` | `MEXC` | `47.78%` | `52.22%` | `0.91` | 25,980,000.00 USD |
| `4H` | `Bitunix` | `50.88%` | `49.12%` | `1.04` | 9,560,000.00 USD |
| `4H` | `Hyperliquid` | `59.14%` | `40.86%` | `1.45` | 78,080,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.66%` | `50.34%` | `0.99` | 1,760,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 23,740.00 USD |
| `4H` | `WhiteBIT` | `94.52%` | `5.48%` | `17.25` | 10,920,000.00 USD |
| `4H` | `HTX` | `47.35%` | `52.65%` | `0.90` | 1,110,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49%` | `51%` | `0.96` | 4,020,000.00 USD |
| `4H` | `Aster` | `36.1%` | `63.9%` | `0.56` | 3,650,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 3,830,000.00 USD |
| `4H` | `Whale Positions` | `51.76%` | `48.24%` | `1.07` | 226,820,000.00 USD |
| `4H` | `Global Accounts` | `51.33%` | `48.67%` | `1.05` | 574,060,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.8801` | `0.8838` | `0.8801` | `0.9093` | `0.8673` | 5,952,763.88 USD | 2,490,126.99 USD | 3,462,636.89 USD | -972,509.89 USD | `-16.34%` | `2B / 19S` |
| `0:00 UTC` | `0.8878` | `0.8837` | `0.8878` | `0.8906` | `0.8749` | 2,004,907.71 USD | 957,094.96 USD | 1,047,812.74 USD | -90,717.78 USD | `-4.52%` | `8B / 10S` |
| `5:00 UTC` | `0.8981` | `0.8950` | `0.8981` | `0.8992` | `0.8880` | 981,791.86 USD | 533,907.73 USD | 447,884.13 USD | 86,023.61 USD | `+8.76%` | `24B / 13S` |
| `0:00 UTC` | `0.9128` | `0.9067` | `0.9128` | `0.9188` | `0.8940` | 5,309,559.22 USD | 3,731,112.91 USD | 1,578,446.31 USD | 2,152,666.61 USD | `+40.54%` | `37B / 0S` |
| `5:00 UTC` | `0.9064` | `0.9085` | `0.9064` | `0.9120` | `0.9046` | 994,017.98 USD | 572,287.48 USD | 421,730.50 USD | 150,556.98 USD | `+15.15%` | `8B / 2S` |
| `0:00 UTC` | `0.9111` | `0.9070` | `0.9111` | `0.9142` | `0.8973` | 1,250,275.83 USD | 633,543.99 USD | 616,731.85 USD | 16,812.14 USD | `+1.34%` | `19B / 16S` |
| `5:00 UTC` | `0.9049` | `0.9049` | `0.9049` | `0.9096` | `0.9016` | 668,740.93 USD | 336,954.59 USD | 331,786.34 USD | 5,168.25 USD | `+0.77%` | `7B / 15S` |
| `0:00 UTC` | `0.9041` | `0.9059` | `0.9041` | `0.9121` | `0.9022` | 1,124,680.00 USD | 451,427.52 USD | 673,252.48 USD | -221,824.96 USD | `-19.72%` | `19B / 6S` |
| `5:00 UTC` | `0.9141` | `0.9167` | `0.9141` | `0.9231` | `0.9118` | 773,293.12 USD | 467,556.11 USD | 305,737.01 USD | 161,819.09 USD | `+20.93%` | `24B / 7S` |
| `0:00 UTC` | `0.9221` | `0.9216` | `0.9221` | `0.9232` | `0.9187` | 640,752.80 USD | 387,877.48 USD | 252,875.32 USD | 135,002.16 USD | `+21.07%` | `4B / 7S` |

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
| `5m` | 6,500.00 USD | 76,250.00 USD | **`ACCUMULATION`** |
| `15m` | 47,360.00 USD | 424,480.00 USD | **`ACCUMULATION`** |
| `30m` | 73,610.00 USD | 145,180.00 USD | **`ACCUMULATION`** |
| `1h` | -54,850.00 USD | 246,770.00 USD | **`ACCUMULATION`** |
| `2h` | 193,250.00 USD | 2,800,000.00 USD | **`ACCUMULATION`** |
| `4h` | -263,650.00 USD | 637,750.00 USD | **`ACCUMULATION`** |
| `6h` | -785,800.00 USD | -4,870,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,050,000.00 USD | -5,650,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,190,000.00 USD | -7,020,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -952,480.00 USD | -6,590,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,270,000.00 USD | -24,150,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -29,690,000.00 USD | -78,030,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.50K` | 15m=`+47.36K` | 1h=`-54.85K` | 24h=`-952.48K`
* Futures Capital Netflows: 5m=`+76.25K` | 15m=`+424.48K` | 1h=`+246.77K` | 24h=`-6.59M`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.8899` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.8428` (Risk Distance: `0.0471` pts)
  * +2.5R Take Profit: `1.01`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.9216` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.9687` (Risk Distance: `0.0471` pts)
  * +2.5R Take Profit: `0.8039`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.9127`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
