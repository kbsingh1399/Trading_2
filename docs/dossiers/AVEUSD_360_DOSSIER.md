# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:46:25 IST` (`2026-10-30 04:16:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `122.73` | **Live Ask Quote**: `123.04` | **Mid Price**: `122.89`
- **Spread Points**: `31.00` | **Spread BPS**: `25.23 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `119.38` | VWAP Z-Score: `+2.25` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `1.60` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `55.07` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `124.87` | Lower -3.00σ Band: `113.90`
  * Upper +2.51σ Band: `123.97` | Lower -2.51σ Band: `114.80`
  * Upper +2.01σ Band: `123.06` | Lower -2.01σ Band: `115.71`
  * Upper +2.00σ Band: `123.04` | Lower -2.00σ Band: `115.73`
  * Upper +1.28σ Band: `121.73` | Lower -1.28σ Band: `117.04`
  * Upper +1.00σ Band: `121.21` | Lower -1.00σ Band: `117.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`121.85` | EMA-20=`121.73` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`124.68` (Slope: `+0.0000`) | EMA-100=`127.54`
  * Institutional Anchors: EMA-144=`128.74` | EMA-200=`129.66` (Slope: `-0.8474`) | EMA-233=`130.17`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `123.39` (Distance: `-0.41%`)
  * Point of Control (POC) = `119.02` (Distance: `+3.25%`)
  * Value Area Low (VAL) = `117.73` (Distance: `+4.37%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.01` | Weekly POC=`135.06` | Weekly VAL=`130.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`123.38` | Low=`122.39`
  * New York Session (13:00-21:00 UTC): High=`123.62` | Low=`122.15`
  * Initial Balance (First Hour): IB High=`123.25` | IB Low=`122.52`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `122.39` - `123.38`
  * Optimal Trade Entry (OTE 0.705): `123.13`
  * Structural Invalidation Anchor (0.786): `123.87`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| --- | **`122.89`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `413` | `0x3ee5...4fab` | `LONG` | 5,323,772.86 USD | `43,303.83` | `77.35` | `122.80` | `74.98` | 1,974,082.82 USD | `+37.08%` | `10X Cross` |
| `745` | `0xecb6...2b00` | `SHORT` | 3,053,825.55 USD | `24,873.35` | `133.17` | `122.80` | `1147.59` | 258,622.86 USD | `+8.47%` | `10X Cross` |
| `804` | `0x0514...bdfe` | `SHORT` | 2,821,640.00 USD | `23,000.00` | `87.41` | `122.80` | `154.84` | -811,160.78 USD | `-28.75%` | `10X Cross` |
| `842` | `0x08c1...1135` | `LONG` | 2,680,172.73 USD | `21,836.18` | `80.89` | `122.80` | `85.68` | 913,838.38 USD | `+34.10%` | `10X Cross` |
| `1034` | `0x0996...0ba6` | `SHORT` | 2,088,790.00 USD | `17,000.00` | `107.97` | `122.80` | `196.58` | -253,216.70 USD | `-12.12%` | `3X Cross` |
| `1145` | `0x45d2...4029` | `SHORT` | 1,930,067.17 USD | `15,721.00` | `118.40` | `122.80` | `2750.65` | -68,675.99 USD | `-3.56%` | `10X Cross` |
| `1156` | `0xbfc7...80b4` | `SHORT` | 1,910,482.90 USD | `15,561.48` | `115.30` | `122.80` | `233.95` | -116,183.58 USD | `-6.08%` | `10X Cross` |
| `1173` | `0x6540...f7b7` | `LONG` | 1,884,091.03 USD | `15,346.51` | `144.40` | `122.80` | `76.39` | -331,884.01 USD | `-17.62%` | `5X Isolated` |
| `1244` | `0x07fd...689d` | `LONG` | 1,773,135.19 USD | `14,442.74` | `148.42` | `122.80` | `0.000000` | -370,474.91 USD | `-20.89%` | `10X Cross` |
| `1459` | `0xcac1...26b3` | `SHORT` | 1,474,560.00 USD | `12,000.00` | `125.37` | `122.80` | `844.89` | 29,880.86 USD | `+2.03%` | `10X Cross` |
| `1466` | `0x12d2...f97f` | `LONG` | 1,469,818.06 USD | `11,961.41` | `133.88` | `122.80` | `0.000000` | -131,586.38 USD | `-8.95%` | `10X Cross` |
| `1479` | `0xeadc...9d55` | `LONG` | 1,452,568.57 USD | `11,823.92` | `89.93` | `122.80` | `0.000000` | 389,212.16 USD | `+26.79%` | `10X Cross` |
| `1647` | `0x9df2...c665` | `SHORT` | 1,274,425.37 USD | `10,380.17` | `133.78` | `122.80` | `3071.73` | 114,283.90 USD | `+8.97%` | `10X Cross` |
| `1704` | `0x3dc9...54b0` | `SHORT` | 1,228,800.00 USD | `10,000.00` | `128.60` | `122.80` | `1824.93` | 57,221.83 USD | `+4.66%` | `10X Cross` |
| `1828` | `0x8af7...fa05` | `SHORT` | 1,121,396.16 USD | `9,133.75` | `131.49` | `122.80` | `2200.66` | 79,584.59 USD | `+7.10%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `137.76` | 52.35 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Long: 0.05K USD at 137.7600 USD [API] | `2026-10-28 20:00:18` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`125.06` (Vol: 442,800.00 USD, Dist: `+1.26%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--5.66%`)
  * 48H Horizon: Short MP=`125.02` (Vol: 442,800.00 USD, Dist: `+1.22%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--5.66%`)
  * 3D Horizon: Short MP=`125.02` (Vol: 442,800.00 USD, Dist: `+1.22%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--5.66%`)
  * 7D Horizon: Short MP=`125.05` (Vol: 442,800.00 USD, Dist: `+1.24%`) | Long MP=`116.46` (Vol: 253,400.00 USD, Dist: `--5.71%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `26.50` | 608.17 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 273.90 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 5,950.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 165.20 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 1,430.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 21,530.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 508.53 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 2,030.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 780.78 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 366.03 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 356.70 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 209.30 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 723.69 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 115.64 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 216.30 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 26,030.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 58,440.00 USD | 8,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 66,790.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 8,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 4,940.00 USD | 8,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 2,470.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 1,100.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 8,750.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 313.47 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 115.94 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 101.08 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,260.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 23,780.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 8,140.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,530.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 10,160.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 19,810.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 3,230,000.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,180,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 9,500.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 15,230.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 8,450.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 50,580.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 2,880.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,930,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 15,140.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 61,940.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,710.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,750.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 20,690.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 2,600.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 16,110.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 94,310.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 45,230.00 USD | 933,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 1,390.00 USD | 888,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 70,650.00 USD | 886,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 39,970.00 USD | 815,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 17,810.00 USD | 776,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 39,350.00 USD | 758,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 12,000.00 USD | 718,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 24,530.00 USD | 706,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 83,870.00 USD | 682,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 35,300.00 USD | 598,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 5,490.00 USD | 563,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,400.00 USD | 557,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 433,810.00 USD | 555,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 18,290.00 USD | 121,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 103,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 52,470.00 USD | 69,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 16,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,960.00 USD | 12,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 775.50 USD | 9,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 8,480.00 USD | 8,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 2,610.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 22,890.00 USD | 25,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 3,260.00 USD | 28,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 170,650.00 USD | 199,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 15,370.00 USD | 214,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 81,620.00 USD | 296,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 1,180.00 USD | 297,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 300,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 300,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 301,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 23,900.00 USD | 325,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,530.00 USD | 328,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 16,070.00 USD | 344,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 567,130.00 USD | 911,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 399.46 USD | 911,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 167.06 USD | 911,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 12,580.00 USD | 924,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 3,550,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 2,200.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 160.88 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 49,950.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 12,770.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 202.99 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 2,650.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 2,080.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 319,420.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 537.65 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 365.44 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 35,220.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 2,330.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 40,290.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 4,960.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,360,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 5,440.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `206.50` | 39,650.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `208.50` | 696.39 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `215.50` | 8,840.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 1,160.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 67,950.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 1,030,000.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `228.50` | 3,560,000.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 2,310.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 259.97 USD | 13,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 64,970.00 USD | 14,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `26.50` | 8,190,000.00 USD | 0.00 USD | 608.17 USD | `-78.60%` | `22.95` |
| `Live` | `Long` | `27.50` | 8,190,000.00 USD | 0.00 USD | 273.90 USD | `-77.79%` | `9.96` |
| `Live` | `Long` | `28.50` | 8,190,000.00 USD | 0.00 USD | 5,950.00 USD | `-76.99%` | `208.76` |
| `Live` | `Long` | `29.50` | 8,190,000.00 USD | 0.00 USD | 165.20 USD | `-76.18%` | `5.60` |
| `Live` | `Long` | `31.50` | 8,190,000.00 USD | 0.00 USD | 1,430.00 USD | `-74.56%` | `45.35` |
| `Live` | `Long` | `33.50` | 8,190,000.00 USD | 0.00 USD | 21,530.00 USD | `-72.95%` | `642.60` |
| `Live` | `Long` | `34.50` | 8,160,000.00 USD | 0.00 USD | 508.53 USD | `-72.14%` | `14.74` |
| `Live` | `Long` | `35.50` | 8,160,000.00 USD | 0.00 USD | 2,030.00 USD | `-71.33%` | `57.05` |
| `Live` | `Long` | `38.50` | 8,160,000.00 USD | 0.00 USD | 780.78 USD | `-68.91%` | `20.28` |
| `Live` | `Long` | `41.50` | 8,160,000.00 USD | 0.00 USD | 366.03 USD | `-66.49%` | `8.82` |
| `Live` | `Long` | `43.50` | 8,160,000.00 USD | 0.00 USD | 356.70 USD | `-64.87%` | `8.20` |
| `Live` | `Long` | `45.50` | 8,160,000.00 USD | 0.00 USD | 209.30 USD | `-63.26%` | `4.60` |
| `Live` | `Long` | `49.50` | 8,160,000.00 USD | 0.00 USD | 723.69 USD | `-60.03%` | `14.62` |
| `Live` | `Long` | `50.50` | 8,160,000.00 USD | 0.00 USD | 115.64 USD | `-59.22%` | `2.29` |
| `Live` | `Long` | `52.50` | 8,160,000.00 USD | 0.00 USD | 216.30 USD | `-57.61%` | `4.12` |
| `Live` | `Long` | `53.50` | 8,160,000.00 USD | 0.00 USD | 26,030.00 USD | `-56.80%` | `486.56` |
| `Live` | `Long` | `54.50` | 8,130,000.00 USD | 0.00 USD | 58,440.00 USD | `-55.99%` | `1,072.26` |
| `Live` | `Long` | `55.50` | 8,070,000.00 USD | 0.00 USD | 66,790.00 USD | `-55.18%` | `1,203.45` |
| `Live` | `Long` | `56.50` | 8,010,000.00 USD | 0.00 USD | 1,510.00 USD | `-54.38%` | `26.66` |
| `Live` | `Long` | `57.50` | 8,010,000.00 USD | 0.00 USD | 4,940.00 USD | `-53.57%` | `85.90` |
| `Live` | `Long` | `58.50` | 8,000,000.00 USD | 0.00 USD | 2,470.00 USD | `-52.76%` | `42.24` |
| `Live` | `Long` | `60.50` | 8,000,000.00 USD | 0.00 USD | 1,690.00 USD | `-51.15%` | `27.87` |
| `Live` | `Long` | `61.50` | 8,000,000.00 USD | 0.00 USD | 168.51 USD | `-50.34%` | `2.74` |
| `Live` | `Long` | `62.50` | 8,000,000.00 USD | 0.00 USD | 1,100.00 USD | `-49.53%` | `17.63` |
| `Live` | `Long` | `63.50` | 8,000,000.00 USD | 0.00 USD | 8,750.00 USD | `-48.72%` | `137.86` |
| `Live` | `Long` | `64.50` | 7,990,000.00 USD | 0.00 USD | 313.47 USD | `-47.92%` | `4.86` |
| `Live` | `Long` | `65.50` | 7,990,000.00 USD | 0.00 USD | 115.94 USD | `-47.11%` | `1.77` |
| `Live` | `Long` | `66.50` | 7,990,000.00 USD | 0.00 USD | 101.08 USD | `-46.30%` | `1.52` |
| `Live` | `Long` | `67.50` | 7,990,000.00 USD | 0.00 USD | 24,320.00 USD | `-45.49%` | `360.30` |
| `Live` | `Long` | `68.50` | 7,960,000.00 USD | 0.00 USD | 7,260.00 USD | `-44.69%` | `105.95` |
| `Live` | `Long` | `69.50` | 7,950,000.00 USD | 0.00 USD | 23,780.00 USD | `-43.88%` | `342.17` |
| `Live` | `Long` | `70.50` | 7,930,000.00 USD | 0.00 USD | 8,140.00 USD | `-43.07%` | `115.49` |
| `Live` | `Long` | `71.50` | 7,920,000.00 USD | 0.00 USD | 1,530.00 USD | `-42.26%` | `21.41` |
| `Live` | `Long` | `72.50` | 7,920,000.00 USD | 0.00 USD | 10,160.00 USD | `-41.46%` | `140.16` |
| `Live` | `Long` | `73.50` | 7,910,000.00 USD | 0.00 USD | 19,810.00 USD | `-40.65%` | `269.58` |
| `Live` | `Long` | `74.50` | 7,890,000.00 USD | 0.00 USD | 3,230,000.00 USD | `-39.84%` | `43,318.03` |
| `Live` | `Long` | `76.50` | 4,660,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-38.23%` | `15,360.04` |
| `Live` | `Long` | `77.50` | 3,490,000.00 USD | 0.00 USD | 9,050.00 USD | `-37.42%` | `116.79` |
| `Live` | `Long` | `78.50` | 3,480,000.00 USD | 0.00 USD | 4,310.00 USD | `-36.61%` | `54.87` |
| `Live` | `Long` | `79.50` | 3,480,000.00 USD | 0.00 USD | 6,790.00 USD | `-35.80%` | `85.43` |
| `Live` | `Long` | `82.50` | 3,470,000.00 USD | 0.00 USD | 9,500.00 USD | `-33.38%` | `115.18` |
| `Live` | `Long` | `83.50` | 3,460,000.00 USD | 0.00 USD | 15,230.00 USD | `-32.57%` | `182.44` |
| `Live` | `Long` | `84.50` | 3,440,000.00 USD | 0.00 USD | 8,450.00 USD | `-31.77%` | `100.00` |
| `Live` | `Long` | `85.50` | 3,440,000.00 USD | 0.00 USD | 50,580.00 USD | `-30.96%` | `591.56` |
| `Live` | `Long` | `86.50` | 3,380,000.00 USD | 0.00 USD | 2,880.00 USD | `-30.15%` | `33.34` |
| `Live` | `Long` | `87.50` | 3,380,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-29.34%` | `22,084.80` |
| `Live` | `Long` | `88.50` | 1,450,000.00 USD | 0.00 USD | 2,050.00 USD | `-28.54%` | `23.18` |
| `Live` | `Long` | `89.50` | 1,450,000.00 USD | 0.00 USD | 15,140.00 USD | `-27.73%` | `169.16` |
| `Live` | `Long` | `90.50` | 1,430,000.00 USD | 0.00 USD | 61,940.00 USD | `-26.92%` | `684.47` |
| `Live` | `Long` | `91.50` | 1,370,000.00 USD | 0.00 USD | 277,710.00 USD | `-26.11%` | `3,035.05` |
| `Live` | `Long` | `92.50` | 1,090,000.00 USD | 0.00 USD | 14,750.00 USD | `-25.31%` | `159.47` |
| `Live` | `Long` | `93.50` | 1,080,000.00 USD | 0.00 USD | 10,990.00 USD | `-24.50%` | `117.52` |
| `Live` | `Long` | `94.50` | 1,070,000.00 USD | 0.00 USD | 20,690.00 USD | `-23.69%` | `218.97` |
| `Live` | `Long` | `95.50` | 1,050,000.00 USD | 0.00 USD | 2,600.00 USD | `-22.88%` | `27.20` |
| `Live` | `Long` | `96.50` | 1,040,000.00 USD | 0.00 USD | 16,110.00 USD | `-22.08%` | `166.97` |
| `Live` | `Long` | `97.50` | 1,030,000.00 USD | 0.00 USD | 94,310.00 USD | `-21.27%` | `967.30` |
| `Live` | `Long` | `98.50` | 933,250.00 USD | 0.00 USD | 45,230.00 USD | `-20.46%` | `459.21` |
| `Live` | `Long` | `99.50` | 888,020.00 USD | 0.00 USD | 1,390.00 USD | `-19.65%` | `14.01` |
| `Live` | `Long` | `100.50` | 886,630.00 USD | 0.00 USD | 70,650.00 USD | `-18.85%` | `703.00` |
| `Live` | `Long` | `101.50` | 815,970.00 USD | 0.00 USD | 39,970.00 USD | `-18.04%` | `393.83` |
| `Live` | `Long` | `102.50` | 776,000.00 USD | 0.00 USD | 17,810.00 USD | `-17.23%` | `173.72` |
| `Live` | `Long` | `103.50` | 758,190.00 USD | 0.00 USD | 39,350.00 USD | `-16.42%` | `380.20` |
| `Live` | `Long` | `104.50` | 718,840.00 USD | 0.00 USD | 12,000.00 USD | `-15.62%` | `114.84` |
| `Live` | `Long` | `105.50` | 706,840.00 USD | 0.00 USD | 24,530.00 USD | `-14.81%` | `232.55` |
| `Live` | `Long` | `106.50` | 682,310.00 USD | 0.00 USD | 83,870.00 USD | `-14.00%` | `787.53` |
| `Live` | `Long` | `107.50` | 598,440.00 USD | 0.00 USD | 35,300.00 USD | `-13.19%` | `328.39` |
| `Live` | `Long` | `108.50` | 563,140.00 USD | 0.00 USD | 5,490.00 USD | `-12.39%` | `50.63` |
| `Live` | `Long` | `109.50` | 557,640.00 USD | 0.00 USD | 2,400.00 USD | `-11.58%` | `21.88` |
| `Live` | `Long` | `110.50` | 555,250.00 USD | 0.00 USD | 433,810.00 USD | `-10.77%` | `3,925.84` |
| `Live` | `Long` | `111.50` | 121,440.00 USD | 0.00 USD | 18,290.00 USD | `-9.96%` | `164.08` |
| `Live` | `Long` | `112.50` | 103,150.00 USD | 0.00 USD | 33,900.00 USD | `-9.16%` | `301.33` |
| `Live` | `Long` | `113.50` | 69,250.00 USD | 0.00 USD | 52,470.00 USD | `-8.35%` | `462.28` |
| `Live` | `Long` | `114.50` | 16,780.00 USD | 0.00 USD | 4,560.00 USD | `-7.54%` | `39.82` |
| `Live` | `Long` | `115.50` | 12,220.00 USD | 0.00 USD | 2,960.00 USD | `-6.73%` | `25.61` |
| `Live` | `Long` | `117.50` | 9,260.00 USD | 0.00 USD | 775.50 USD | `-5.12%` | `6.60` |
| `Live` | `Long` | `119.50` | 8,480.00 USD | 0.00 USD | 8,480.00 USD | `-3.50%` | `71.00` |
| `Live` | `Short` | `125.50` | 2,610.00 USD | 2,610.00 USD | 0.00 USD | `+1.34%` | `20.77` |
| `Live` | `Short` | `126.50` | 25,490.00 USD | 22,890.00 USD | 0.00 USD | `+2.15%` | `180.91` |
| `Live` | `Short` | `129.50` | 28,750.00 USD | 3,260.00 USD | 0.00 USD | `+4.57%` | `25.14` |
| `Live` | `Short` | `130.50` | 199,390.00 USD | 170,650.00 USD | 0.00 USD | `+5.38%` | `1,307.63` |
| `Live` | `Short` | `133.50` | 214,770.00 USD | 15,370.00 USD | 0.00 USD | `+7.80%` | `115.15` |
| `Live` | `Short` | `136.50` | 296,390.00 USD | 81,620.00 USD | 0.00 USD | `+10.22%` | `597.95` |
| `Live` | `Short` | `137.50` | 297,560.00 USD | 1,180.00 USD | 0.00 USD | `+11.03%` | `8.55` |
| `Live` | `Short` | `138.50` | 300,410.00 USD | 2,850.00 USD | 0.00 USD | `+11.84%` | `20.56` |
| `Live` | `Short` | `139.50` | 300,510.00 USD | 100.44 USD | 0.00 USD | `+12.65%` | `0.72` |
| `Live` | `Short` | `140.50` | 301,660.00 USD | 1,150.00 USD | 0.00 USD | `+13.45%` | `8.19` |
| `Live` | `Short` | `141.50` | 325,560.00 USD | 23,900.00 USD | 0.00 USD | `+14.26%` | `168.93` |
| `Live` | `Short` | `142.50` | 328,090.00 USD | 2,530.00 USD | 0.00 USD | `+15.07%` | `17.73` |
| `Live` | `Short` | `143.50` | 344,160.00 USD | 16,070.00 USD | 0.00 USD | `+15.88%` | `111.98` |
| `Live` | `Short` | `145.50` | 911,290.00 USD | 567,130.00 USD | 0.00 USD | `+17.49%` | `3,897.82` |
| `Live` | `Short` | `148.50` | 911,690.00 USD | 399.46 USD | 0.00 USD | `+19.91%` | `2.69` |
| `Live` | `Short` | `150.50` | 911,860.00 USD | 167.06 USD | 0.00 USD | `+21.53%` | `1.11` |
| `Live` | `Short` | `151.50` | 924,440.00 USD | 12,580.00 USD | 0.00 USD | `+22.34%` | `83.02` |
| `Live` | `Short` | `154.50` | 4,480,000.00 USD | 3,550,000.00 USD | 0.00 USD | `+24.76%` | `23,000.00` |
| `Live` | `Short` | `155.50` | 4,480,000.00 USD | 2,200.00 USD | 0.00 USD | `+25.57%` | `14.13` |
| `Live` | `Short` | `158.50` | 4,480,000.00 USD | 1,480.00 USD | 0.00 USD | `+27.99%` | `9.36` |
| `Live` | `Short` | `162.50` | 4,480,000.00 USD | 160.88 USD | 0.00 USD | `+31.22%` | `0.99` |
| `Live` | `Short` | `166.50` | 4,530,000.00 USD | 49,950.00 USD | 0.00 USD | `+34.45%` | `300.00` |
| `Live` | `Short` | `167.50` | 4,540,000.00 USD | 12,770.00 USD | 0.00 USD | `+35.26%` | `76.26` |
| `Live` | `Short` | `173.50` | 4,540,000.00 USD | 202.99 USD | 0.00 USD | `+40.10%` | `1.17` |
| `Live` | `Short` | `174.50` | 4,550,000.00 USD | 2,650.00 USD | 0.00 USD | `+40.91%` | `15.20` |
| `Live` | `Short` | `175.50` | 4,550,000.00 USD | 5,620.00 USD | 0.00 USD | `+41.72%` | `32.04` |
| `Live` | `Short` | `176.50` | 4,560,000.00 USD | 2,080.00 USD | 0.00 USD | `+42.52%` | `11.81` |
| `Live` | `Short` | `181.50` | 4,870,000.00 USD | 319,420.00 USD | 0.00 USD | `+46.56%` | `1,759.87` |
| `Live` | `Short` | `183.50` | 4,880,000.00 USD | 537.65 USD | 0.00 USD | `+48.18%` | `2.93` |
| `Live` | `Short` | `185.50` | 4,880,000.00 USD | 365.44 USD | 0.00 USD | `+49.79%` | `1.97` |
| `Live` | `Short` | `186.50` | 4,910,000.00 USD | 35,220.00 USD | 0.00 USD | `+50.60%` | `188.85` |
| `Live` | `Short` | `187.50` | 4,910,000.00 USD | 2,330.00 USD | 0.00 USD | `+51.41%` | `12.41` |
| `Live` | `Short` | `189.50` | 4,950,000.00 USD | 40,290.00 USD | 0.00 USD | `+53.02%` | `212.59` |
| `Live` | `Short` | `191.50` | 4,960,000.00 USD | 4,960.00 USD | 0.00 USD | `+54.64%` | `25.90` |
| `Live` | `Short` | `196.50` | 8,320,000.00 USD | 3,360,000.00 USD | 0.00 USD | `+58.67%` | `17,092.85` |
| `Live` | `Short` | `200.50` | 8,330,000.00 USD | 9,850.00 USD | 0.00 USD | `+61.90%` | `49.15` |
| `Live` | `Short` | `201.50` | 8,330,000.00 USD | 5,440.00 USD | 0.00 USD | `+62.71%` | `27.00` |
| `Live` | `Short` | `203.50` | 8,330,000.00 USD | 372.41 USD | 0.00 USD | `+64.32%` | `1.83` |
| `Live` | `Short` | `205.50` | 8,420,000.00 USD | 84,610.00 USD | 0.00 USD | `+65.94%` | `411.72` |
| `Live` | `Short` | `206.50` | 8,460,000.00 USD | 39,650.00 USD | 0.00 USD | `+66.75%` | `192.00` |
| `Live` | `Short` | `208.50` | 8,460,000.00 USD | 696.39 USD | 0.00 USD | `+68.36%` | `3.34` |
| `Live` | `Short` | `210.50` | 8,460,000.00 USD | 151.56 USD | 0.00 USD | `+69.98%` | `0.72` |
| `Live` | `Short` | `215.50` | 8,470,000.00 USD | 8,840.00 USD | 0.00 USD | `+74.01%` | `41.00` |
| `Live` | `Short` | `220.50` | 8,470,000.00 USD | 2,000.00 USD | 0.00 USD | `+78.05%` | `9.06` |
| `Live` | `Short` | `225.50` | 8,470,000.00 USD | 1,160.00 USD | 0.00 USD | `+82.09%` | `5.15` |
| `Live` | `Short` | `226.50` | 8,540,000.00 USD | 67,950.00 USD | 0.00 USD | `+82.90%` | `300.00` |
| `Live` | `Short` | `227.50` | 9,560,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+83.70%` | `4,508.67` |
| `Live` | `Short` | `228.50` | 13,120,000.00 USD | 3,560,000.00 USD | 0.00 USD | `+84.51%` | `15,561.48` |
| `Live` | `Short` | `230.50` | 13,120,000.00 USD | 2,310.00 USD | 0.00 USD | `+86.13%` | `10.00` |
| `Live` | `Short` | `232.50` | 13,940,000.00 USD | 818,270.00 USD | 0.00 USD | `+87.74%` | `3,519.45` |
| `Live` | `Short` | `238.50` | 13,940,000.00 USD | 259.97 USD | 0.00 USD | `+92.59%` | `1.09` |
| `Live` | `Short` | `240.50` | 14,000,000.00 USD | 64,970.00 USD | 0.00 USD | `+94.20%` | `270.16` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-16.12K` | Last 24h: `15.72K` | Last 3d: `55.76K` | Last 7d: `119.40K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0064%` | **USDT OKX** | `-0.0000%` |
| **USDT Bybit** | `-0.0411%` | **USDT KuCoin** | `-0.0015%` |
| **USDT MEXC** | `0.0065%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0037%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0023%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `120.00` | `119.47` | `120.00` | `120.09` | `118.78` | 1,546,202.74 USD | 806,296.59 USD | 739,906.15 USD | 66,390.44 USD | `+4.29%` | `35B / 13S` |
| `0:00 UTC` | `119.72` | `119.95` | `119.72` | `120.84` | `119.12` | 2,078,229.74 USD | 977,317.91 USD | 1,100,911.84 USD | -123,593.93 USD | `-5.95%` | `39B / 19S` |
| `5:00 UTC` | `121.50` | `121.18` | `121.50` | `121.84` | `120.55` | 2,502,423.84 USD | 1,511,661.07 USD | 990,762.77 USD | 520,898.29 USD | `+20.82%` | `32B / 7S` |
| `0:00 UTC` | `121.75` | `121.55` | `121.75` | `121.91` | `120.97` | 1,387,351.12 USD | 687,614.69 USD | 699,736.43 USD | -12,121.73 USD | `-0.87%` | `13B / 15S` |
| `5:00 UTC` | `121.59` | `121.57` | `121.59` | `122.09` | `121.05` | 2,442,757.80 USD | 1,676,951.27 USD | 765,806.53 USD | 911,144.74 USD | `+37.30%` | `26B / 7S` |
| `0:00 UTC` | `122.00` | `121.97` | `122.00` | `122.50` | `121.59` | 2,148,114.65 USD | 949,251.03 USD | 1,198,863.61 USD | -249,612.58 USD | `-11.62%` | `15B / 8S` |
| `5:00 UTC` | `122.60` | `122.32` | `122.60` | `123.18` | `121.75` | 1,556,143.15 USD | 808,945.27 USD | 747,197.89 USD | 61,747.38 USD | `+3.97%` | `36B / 18S` |
| `0:00 UTC` | `123.50` | `123.59` | `123.50` | `124.12` | `122.77` | 1,930,466.83 USD | 1,169,577.61 USD | 760,889.22 USD | 408,688.38 USD | `+21.17%` | `33B / 9S` |
| `5:00 UTC` | `124.25` | `124.03` | `124.25` | `124.45` | `123.66` | 1,500,731.33 USD | 697,230.09 USD | 803,501.24 USD | -106,271.15 USD | `-7.08%` | `8B / 7S` |
| `0:00 UTC` | `123.52` | `123.25` | `123.52` | `123.91` | `122.69` | 1,965,022.34 USD | 973,390.79 USD | 991,631.54 USD | -18,240.75 USD | `-0.93%` | `17B / 23S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:02` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `132.86` | 0.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.95` | 1,200.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 20K AAVE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `130.77` | 3,200.00 USD | 0.00 USD |
| `10-28 19:42` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `131.45` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.5` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `131.08` | 3,500.00 USD | 0.00 USD |
| `10-28 19:06` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.72` | 3,400.00 USD | 0.00 USD |
| `10-28 18:47` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `131.61` | 4,500.00 USD | 0.00 USD |
| `10-28 18:36` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.46` | 1,300.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.24` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `133.63` | 5,700.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `133.04` | 0.00 USD | 0.00 USD |
| `10-28 16:41` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `134.42` | 0.00 USD | 0.00 USD |
| `10-28 15:53` | `Range 0.5` | `Divergence` | **`BULLISH`** | Drop without taker selling | `135.39` | 0.00 USD | 0.00 USD |
| `10-28 13:58` | `Volume 20K AAVE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `136.84` | 0.00 USD | 0.00 USD |
| `10-28 13:36` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `135.33` | 3,200.00 USD | 0.00 USD |
| `10-28 11:03` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.16` | 3,800.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `134.87` | 0.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.37` | 1,400.00 USD | 0.00 USD |
| `10-28 09:16` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `136.00` | 1,200.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `136.00` | 3,700.00 USD | 0.00 USD |
| `10-28 08:34` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.67` | 3,800.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.22` | 0.00 USD | 0.00 USD |
| `10-28 08:15` | `Volume 20K AAVE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.66` | 0.00 USD | 0.00 USD |
| `10-28 08:09` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.15` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `135.87` | 3,900.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.5` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `135.17` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -58,810.00 USD | -413,630.00 USD | **`DISTRIBUTION`** |
| `15m` | -167,060.00 USD | -287,020.00 USD | **`DISTRIBUTION`** |
| `30m` | -180,520.00 USD | -278,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -117,130.00 USD | -284,930.00 USD | **`DISTRIBUTION`** |
| `2h` | 73,590.00 USD | 622,210.00 USD | **`ACCUMULATION`** |
| `4h` | -1,000,000.00 USD | -956,490.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,570,000.00 USD | -5,790,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,370,000.00 USD | -10,370,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,420,000.00 USD | -12,670,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -6,980,000.00 USD | -11,670,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -29,080,000.00 USD | -50,710,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -116,490,000.00 USD | -103,190,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-58.81K` | 15m=`-167.06K` | 1h=`-117.13K` | 24h=`-6.98M`
* Futures Capital Netflows: 5m=`-413.63K` | 15m=`-287.02K` | 1h=`-284.93K` | 24h=`-11.67M`
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
  * `2026-10-30 09:09:49 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:42:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:41:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:43:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:43:49 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:43:49 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `117.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `115.35` (Risk Distance: `2.38` pts)
  * +2.5R Take Profit: `123.68`
  * Mathematical Lot Sizing: **`4.20 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `123.39` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `125.77` (Risk Distance: `2.38` pts)
  * +2.5R Take Profit: `117.44`
  * Mathematical Lot Sizing: **`4.20 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`123.87`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
