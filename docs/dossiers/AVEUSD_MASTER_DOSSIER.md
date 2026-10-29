# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:28:57 IST` (`2026-10-29 22:58:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `120.10` | **Live Ask Quote**: `120.46` | **Mid Price**: `120.28`
- **Spread Points**: `36.00` | **Spread BPS**: `29.93 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `130.75` | VWAP Z-Score: `-2.10` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `2.02` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `29.85` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `142.13` | Lower -3.00σ Band: `119.38`
  * Upper +2.51σ Band: `140.27` | Lower -2.51σ Band: `121.23`
  * Upper +2.01σ Band: `138.38` | Lower -2.01σ Band: `123.13`
  * Upper +2.00σ Band: `138.34` | Lower -2.00σ Band: `123.17`
  * Upper +1.28σ Band: `135.61` | Lower -1.28σ Band: `125.90`
  * Upper +1.00σ Band: `134.55` | Lower -1.00σ Band: `126.96`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`124.73` | EMA-20=`127.62` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`130.32` (Slope: `+0.0000`) | EMA-100=`131.36`
  * Institutional Anchors: EMA-144=`131.70` | EMA-200=`131.93` (Slope: `-0.5796`) | EMA-233=`132.13`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`121.49` | Weekly High=`138.47` | Weekly Low=`121.49`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `125.04` (Distance: `-3.87%`)
  * Point of Control (POC) = `123.64` (Distance: `-2.79%`)
  * Value Area Low (VAL) = `121.68` (Distance: `-1.22%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`135.92` | Weekly POC=`135.30` | Weekly VAL=`131.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`119.80`
  * London Session (08:00-16:00 UTC): High=`120.76` | Low=`119.80`
  * New York Session (13:00-21:00 UTC): High=`121.00` | Low=`119.56`
  * Initial Balance (First Hour): IB High=`120.64` | IB Low=`119.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `119.80` - `120.76`
  * Optimal Trade Entry (OTE 0.705): `120.52`
  * Structural Invalidation Anchor (0.786): `121.24`

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
| --- | **`120.28`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:26:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `423` | `0x3ee5...4fab` | `LONG` | 5,183,035.41 USD | `43,303.83` | `77.35` | `119.77` | `98.90` | 1,833,345.37 USD | `+35.37%` | `10X Cross` |
| `810` | `0x0514...bdfe` | `SHORT` | 2,769,890.00 USD | `23,000.00` | `87.41` | `119.77` | `188.79` | -759,410.78 USD | `-27.42%` | `10X Cross` |
| `853` | `0x08c1...1135` | `LONG` | 2,613,572.38 USD | `21,836.18` | `80.89` | `119.77` | `82.03` | 847,238.03 USD | `+32.42%` | `10X Cross` |
| `1064` | `0xecb6...2b00` | `SHORT` | 2,050,941.46 USD | `17,148.34` | `139.77` | `119.77` | `1756.22` | 345,860.90 USD | `+16.86%` | `10X Cross` |
| `1072` | `0x0996...0ba6` | `SHORT` | 2,041,700.00 USD | `17,000.00` | `107.97` | `119.77` | `196.59` | -206,126.70 USD | `-10.10%` | `3X Cross` |
| `1181` | `0x45d2...4029` | `SHORT` | 1,890,135.83 USD | `15,721.00` | `118.40` | `119.77` | `2713.99` | -28,744.65 USD | `-1.52%` | `10X Cross` |
| `1191` | `0xbfc7...80b4` | `SHORT` | 1,862,553.54 USD | `15,561.48` | `115.30` | `119.77` | `354.97` | -68,254.22 USD | `-3.66%` | `10X Cross` |
| `1217` | `0x6540...f7b7` | `LONG` | 1,828,712.00 USD | `15,200.00` | `144.85` | `119.77` | `84.60` | -372,987.30 USD | `-20.40%` | `5X Isolated` |
| `1277` | `0x07fd...689d` | `LONG` | 1,737,351.19 USD | `14,480.34` | `149.05` | `119.77` | `0.000000` | -420,976.81 USD | `-24.23%` | `10X Cross` |
| `1509` | `0xcac1...26b3` | `SHORT` | 1,441,200.00 USD | `12,000.00` | `125.37` | `119.77` | `841.14` | 63,240.86 USD | `+4.39%` | `10X Cross` |
| `1541` | `0xeadc...9d55` | `LONG` | 1,415,323.22 USD | `11,823.92` | `89.93` | `119.77` | `0.000000` | 351,966.81 USD | `+24.87%` | `10X Cross` |
| `1687` | `0x9df2...c665` | `SHORT` | 1,251,452.59 USD | `10,430.51` | `133.81` | `119.77` | `3136.34` | 144,306.43 USD | `+11.53%` | `10X Cross` |
| `1741` | `0x3dc9...54b0` | `SHORT` | 1,199,200.00 USD | `10,000.00` | `128.60` | `119.77` | `1785.08` | 86,821.83 USD | `+7.24%` | `10X Cross` |
| `1862` | `0x8af7...fa05` | `SHORT` | 1,099,064.14 USD | `9,133.75` | `131.49` | `119.77` | `2225.20` | 101,916.61 USD | `+9.27%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `133.00` | 30.59 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Long: 0.03K USD at 133.0000 USD [API] | `2026-08-24 17:32:59` |
| `ANNOUNCEMENT` | `INFO` | `133.02` | 732.94 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Long: 0.73K USD at 133.0200 USD [API] | `2026-08-24 17:32:59` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`126.67` (Vol: 411,400.00 USD, Dist: `+4.24%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`128.76` (Vol: 368,100.00 USD, Dist: `+5.97%`) | Long MP=`121.36` (Vol: 266,900.00 USD, Dist: `--0.12%`)
  * 3D Horizon: Short MP=`128.76` (Vol: 368,100.00 USD, Dist: `+5.97%`) | Long MP=`121.36` (Vol: 266,900.00 USD, Dist: `--0.12%`)
  * 7D Horizon: Short MP=`139.75` (Vol: 348,700.00 USD, Dist: `+15.01%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `25.50` | 391.43 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 1,850.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 585.20 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 36,100.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 181.78 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 101.11 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 20,810.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 702.76 USD | 10,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 1,470.00 USD | 10,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 5,590.00 USD | 10,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 938.12 USD | 10,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 158.34 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 158.10 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 276.70 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 191.90 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 4,630.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 10,560.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 4,580.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 487.90 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 2,410.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 323.75 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 488.95 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 2,350.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 31,310.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 6,630.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,620.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 3,000.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 13,210.00 USD | 9,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 36,720.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 13,770.00 USD | 9,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,330.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 444.47 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 15,950.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,460.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 9,270.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,420.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 109,030.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 21,120.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 53,710.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 1,890,000.00 USD | 9,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 17,470.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,350,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 1,510.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,720.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 12,350.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 74,260.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 70,990.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 7,130.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 8,100.00 USD | 5,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 97,460.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 4,300,000.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 77,270.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 2,540.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 2,290.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 12,290.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 5,200.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 16,730.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 29,140.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 15,090.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 47,810.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 51,410.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 14,990.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 616,710.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 6,680.00 USD | 653,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 2,560.00 USD | 646,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 116,580.00 USD | 644,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 312,900.00 USD | 527,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 12,850.00 USD | 214,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 60,120.00 USD | 201,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 26,610.00 USD | 141,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 16,420.00 USD | 115,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 36,340.00 USD | 98,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 27,340.00 USD | 62,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 293,950.00 USD | 293,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 20,180.00 USD | 34,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `123.50` | 14,190.00 USD | 14,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 598.84 USD | 598.84 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 5,430.00 USD | 299,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 3,580.00 USD | 302,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 4,140.00 USD | 307,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 10,680.00 USD | 317,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 26,350.00 USD | 344,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 30,380.00 USD | 374,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 374,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 8,280.00 USD | 382,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 998.99 USD | 383,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 2,730.00 USD | 386,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 387,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 84,040.00 USD | 471,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,520.00 USD | 473,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 167.06 USD | 474,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 237.85 USD | 474,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 594,420.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 32,450.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 1,900.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 592,910.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 1,850.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 56,700.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 959.40 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 4,340,000.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 34,730.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 4,180.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 358.05 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 286.38 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 4,670.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 1,500.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 40,660.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 11,800.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 20,150.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 91,230.00 USD | 9,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `209.50` | 15,080.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `211.50` | 25,380.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `217.50` | 8,920.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `221.50` | 1,110.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 9,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 68,250.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 2,330.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 192.29 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 5,050.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 382.39 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `241.50` | 419,350.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 647.48 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `244.50` | 845.97 USD | 10,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `249.50` | 132.24 USD | 10,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 10,100,000.00 USD | 0.00 USD | 391.43 USD | `-79.60%` | `15.35` |
| `Live` | `Long` | `26.50` | 10,100,000.00 USD | 0.00 USD | 1,850.00 USD | `-78.80%` | `70.00` |
| `Live` | `Long` | `27.50` | 10,100,000.00 USD | 0.00 USD | 585.20 USD | `-78.00%` | `21.28` |
| `Live` | `Long` | `29.50` | 10,100,000.00 USD | 0.00 USD | 36,100.00 USD | `-76.40%` | `1,223.59` |
| `Live` | `Long` | `30.50` | 10,060,000.00 USD | 0.00 USD | 181.78 USD | `-75.59%` | `5.96` |
| `Live` | `Long` | `31.50` | 10,060,000.00 USD | 0.00 USD | 101.11 USD | `-74.79%` | `3.21` |
| `Live` | `Long` | `32.50` | 10,060,000.00 USD | 0.00 USD | 20,810.00 USD | `-73.99%` | `640.20` |
| `Live` | `Long` | `34.50` | 10,040,000.00 USD | 0.00 USD | 702.76 USD | `-72.39%` | `20.37` |
| `Live` | `Long` | `37.50` | 10,040,000.00 USD | 0.00 USD | 1,470.00 USD | `-69.99%` | `39.17` |
| `Live` | `Long` | `38.50` | 10,040,000.00 USD | 0.00 USD | 5,590.00 USD | `-69.19%` | `145.09` |
| `Live` | `Long` | `39.50` | 10,040,000.00 USD | 0.00 USD | 938.12 USD | `-68.39%` | `23.75` |
| `Live` | `Long` | `45.50` | 10,030,000.00 USD | 0.00 USD | 158.34 USD | `-63.59%` | `3.48` |
| `Live` | `Long` | `46.50` | 10,030,000.00 USD | 0.00 USD | 158.10 USD | `-62.79%` | `3.40` |
| `Live` | `Long` | `49.50` | 10,030,000.00 USD | 0.00 USD | 276.70 USD | `-60.39%` | `5.59` |
| `Live` | `Long` | `50.50` | 10,030,000.00 USD | 0.00 USD | 191.90 USD | `-59.59%` | `3.80` |
| `Live` | `Long` | `52.50` | 10,030,000.00 USD | 0.00 USD | 4,630.00 USD | `-57.99%` | `88.27` |
| `Live` | `Long` | `54.50` | 10,030,000.00 USD | 0.00 USD | 805.51 USD | `-56.39%` | `14.78` |
| `Live` | `Long` | `55.50` | 10,030,000.00 USD | 0.00 USD | 1,410.00 USD | `-55.59%` | `25.36` |
| `Live` | `Long` | `56.50` | 10,030,000.00 USD | 0.00 USD | 10,560.00 USD | `-54.79%` | `186.85` |
| `Live` | `Long` | `57.50` | 10,020,000.00 USD | 0.00 USD | 4,580.00 USD | `-53.99%` | `79.67` |
| `Live` | `Long` | `58.50` | 10,010,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.19%` | `27.49` |
| `Live` | `Long` | `59.50` | 10,010,000.00 USD | 0.00 USD | 487.90 USD | `-52.39%` | `8.20` |
| `Live` | `Long` | `60.50` | 10,010,000.00 USD | 0.00 USD | 2,410.00 USD | `-51.59%` | `39.82` |
| `Live` | `Long` | `61.50` | 10,010,000.00 USD | 0.00 USD | 168.51 USD | `-50.79%` | `2.74` |
| `Live` | `Long` | `62.50` | 10,010,000.00 USD | 0.00 USD | 323.75 USD | `-49.99%` | `5.18` |
| `Live` | `Long` | `63.50` | 10,010,000.00 USD | 0.00 USD | 488.95 USD | `-49.19%` | `7.70` |
| `Live` | `Long` | `66.50` | 10,010,000.00 USD | 0.00 USD | 2,350.00 USD | `-46.79%` | `35.29` |
| `Live` | `Long` | `67.50` | 10,000,000.00 USD | 0.00 USD | 31,310.00 USD | `-45.99%` | `463.92` |
| `Live` | `Long` | `68.50` | 9,970,000.00 USD | 0.00 USD | 6,630.00 USD | `-45.19%` | `96.85` |
| `Live` | `Long` | `69.50` | 9,970,000.00 USD | 0.00 USD | 18,620.00 USD | `-44.39%` | `267.94` |
| `Live` | `Long` | `70.50` | 9,950,000.00 USD | 0.00 USD | 3,000.00 USD | `-43.59%` | `42.51` |
| `Live` | `Long` | `71.50` | 9,940,000.00 USD | 0.00 USD | 13,210.00 USD | `-42.79%` | `184.76` |
| `Live` | `Long` | `72.50` | 9,930,000.00 USD | 0.00 USD | 36,720.00 USD | `-41.99%` | `506.50` |
| `Live` | `Long` | `73.50` | 9,890,000.00 USD | 0.00 USD | 13,770.00 USD | `-41.19%` | `187.39` |
| `Live` | `Long` | `74.50` | 9,880,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.39%` | `14.20` |
| `Live` | `Long` | `75.50` | 9,880,000.00 USD | 0.00 USD | 1,330.00 USD | `-39.59%` | `17.61` |
| `Live` | `Long` | `76.50` | 9,880,000.00 USD | 0.00 USD | 444.47 USD | `-38.79%` | `5.81` |
| `Live` | `Long` | `77.50` | 9,880,000.00 USD | 0.00 USD | 15,950.00 USD | `-37.99%` | `205.86` |
| `Live` | `Long` | `78.50` | 9,860,000.00 USD | 0.00 USD | 4,460.00 USD | `-37.19%` | `56.78` |
| `Live` | `Long` | `79.50` | 9,860,000.00 USD | 0.00 USD | 9,270.00 USD | `-36.39%` | `116.57` |
| `Live` | `Long` | `82.50` | 9,850,000.00 USD | 0.00 USD | 1,420.00 USD | `-33.99%` | `17.22` |
| `Live` | `Long` | `83.50` | 9,850,000.00 USD | 0.00 USD | 109,030.00 USD | `-33.19%` | `1,305.69` |
| `Live` | `Long` | `84.50` | 9,740,000.00 USD | 0.00 USD | 21,120.00 USD | `-32.39%` | `250.00` |
| `Live` | `Long` | `85.50` | 9,720,000.00 USD | 0.00 USD | 53,710.00 USD | `-31.59%` | `628.17` |
| `Live` | `Long` | `86.50` | 9,660,000.00 USD | 0.00 USD | 1,890,000.00 USD | `-30.79%` | `21,863.92` |
| `Live` | `Long` | `87.50` | 7,770,000.00 USD | 0.00 USD | 17,470.00 USD | `-29.99%` | `199.64` |
| `Live` | `Long` | `88.50` | 7,750,000.00 USD | 0.00 USD | 2,050.00 USD | `-29.19%` | `23.18` |
| `Live` | `Long` | `89.50` | 7,750,000.00 USD | 0.00 USD | 1,350,000.00 USD | `-28.38%` | `15,115.05` |
| `Live` | `Long` | `90.50` | 6,400,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.58%` | `16.71` |
| `Live` | `Long` | `91.50` | 6,400,000.00 USD | 0.00 USD | 277,720.00 USD | `-26.78%` | `3,035.15` |
| `Live` | `Long` | `92.50` | 6,120,000.00 USD | 0.00 USD | 12,350.00 USD | `-25.98%` | `133.49` |
| `Live` | `Long` | `93.50` | 6,110,000.00 USD | 0.00 USD | 74,260.00 USD | `-25.18%` | `794.22` |
| `Live` | `Long` | `94.50` | 6,030,000.00 USD | 0.00 USD | 70,990.00 USD | `-24.38%` | `751.20` |
| `Live` | `Long` | `95.50` | 5,960,000.00 USD | 0.00 USD | 7,130.00 USD | `-23.58%` | `74.65` |
| `Live` | `Long` | `96.50` | 5,960,000.00 USD | 0.00 USD | 8,100.00 USD | `-22.78%` | `83.96` |
| `Live` | `Long` | `97.50` | 5,950,000.00 USD | 0.00 USD | 97,460.00 USD | `-21.98%` | `999.59` |
| `Live` | `Long` | `98.50` | 5,850,000.00 USD | 0.00 USD | 4,300,000.00 USD | `-21.18%` | `43,704.37` |
| `Live` | `Long` | `99.50` | 1,540,000.00 USD | 0.00 USD | 77,270.00 USD | `-20.38%` | `776.58` |
| `Live` | `Long` | `100.50` | 1,470,000.00 USD | 0.00 USD | 2,540.00 USD | `-19.58%` | `25.31` |
| `Live` | `Long` | `101.50` | 1,470,000.00 USD | 0.00 USD | 2,290.00 USD | `-18.78%` | `22.59` |
| `Live` | `Long` | `102.50` | 1,460,000.00 USD | 0.00 USD | 12,290.00 USD | `-17.98%` | `119.89` |
| `Live` | `Long` | `103.50` | 1,450,000.00 USD | 0.00 USD | 5,200.00 USD | `-17.18%` | `50.23` |
| `Live` | `Long` | `104.50` | 1,450,000.00 USD | 0.00 USD | 16,730.00 USD | `-16.38%` | `160.11` |
| `Live` | `Long` | `105.50` | 1,430,000.00 USD | 0.00 USD | 29,140.00 USD | `-15.58%` | `276.21` |
| `Live` | `Long` | `106.50` | 1,400,000.00 USD | 0.00 USD | 15,090.00 USD | `-14.78%` | `141.65` |
| `Live` | `Long` | `107.50` | 1,380,000.00 USD | 0.00 USD | 47,810.00 USD | `-13.98%` | `444.71` |
| `Live` | `Long` | `108.50` | 1,340,000.00 USD | 0.00 USD | 51,410.00 USD | `-13.18%` | `473.80` |
| `Live` | `Long` | `109.50` | 1,290,000.00 USD | 0.00 USD | 14,990.00 USD | `-12.38%` | `136.91` |
| `Live` | `Long` | `110.50` | 1,270,000.00 USD | 0.00 USD | 616,710.00 USD | `-11.58%` | `5,581.07` |
| `Live` | `Long` | `111.50` | 653,370.00 USD | 0.00 USD | 6,680.00 USD | `-10.78%` | `59.90` |
| `Live` | `Long` | `112.50` | 646,690.00 USD | 0.00 USD | 2,560.00 USD | `-9.98%` | `22.73` |
| `Live` | `Long` | `113.50` | 644,130.00 USD | 0.00 USD | 116,580.00 USD | `-9.18%` | `1,027.17` |
| `Live` | `Long` | `114.50` | 527,550.00 USD | 0.00 USD | 312,900.00 USD | `-8.38%` | `2,732.78` |
| `Live` | `Long` | `115.50` | 214,650.00 USD | 0.00 USD | 12,850.00 USD | `-7.58%` | `111.23` |
| `Live` | `Long` | `116.50` | 201,800.00 USD | 0.00 USD | 60,120.00 USD | `-6.78%` | `516.07` |
| `Live` | `Long` | `117.50` | 141,680.00 USD | 0.00 USD | 26,610.00 USD | `-5.98%` | `226.50` |
| `Live` | `Long` | `118.50` | 115,060.00 USD | 0.00 USD | 16,420.00 USD | `-5.18%` | `138.56` |
| `Live` | `Long` | `119.50` | 98,640.00 USD | 0.00 USD | 36,340.00 USD | `-4.38%` | `304.11` |
| `Live` | `Long` | `120.50` | 62,300.00 USD | 0.00 USD | 27,340.00 USD | `-3.58%` | `226.86` |
| `Live` | `Short` | `121.50` | 293,950.00 USD | 293,950.00 USD | 0.00 USD | `-2.78%` | `2,419.38` |
| `Live` | `Long` | `122.50` | 34,970.00 USD | 0.00 USD | 20,180.00 USD | `-1.98%` | `164.71` |
| `Live` | `Long` | `123.50` | 14,790.00 USD | 0.00 USD | 14,190.00 USD | `-1.18%` | `114.90` |
| `Live` | `Long` | `124.50` | 598.84 USD | 0.00 USD | 598.84 USD | `-0.38%` | `4.81` |
| `Live` | `Short` | `127.50` | 299,380.00 USD | 5,430.00 USD | 0.00 USD | `+2.02%` | `42.55` |
| `Live` | `Short` | `131.50` | 302,960.00 USD | 3,580.00 USD | 0.00 USD | `+5.22%` | `27.20` |
| `Live` | `Short` | `132.50` | 307,100.00 USD | 4,140.00 USD | 0.00 USD | `+6.02%` | `31.26` |
| `Live` | `Short` | `133.50` | 317,780.00 USD | 10,680.00 USD | 0.00 USD | `+6.82%` | `80.00` |
| `Live` | `Short` | `134.50` | 344,130.00 USD | 26,350.00 USD | 0.00 USD | `+7.62%` | `195.93` |
| `Live` | `Short` | `135.50` | 374,510.00 USD | 30,380.00 USD | 0.00 USD | `+8.42%` | `224.18` |
| `Live` | `Short` | `139.50` | 374,610.00 USD | 100.44 USD | 0.00 USD | `+11.62%` | `0.72` |
| `Live` | `Short` | `140.50` | 382,890.00 USD | 8,280.00 USD | 0.00 USD | `+12.42%` | `58.93` |
| `Live` | `Short` | `141.50` | 383,890.00 USD | 998.99 USD | 0.00 USD | `+13.22%` | `7.06` |
| `Live` | `Short` | `144.50` | 386,620.00 USD | 2,730.00 USD | 0.00 USD | `+15.62%` | `18.91` |
| `Live` | `Short` | `145.50` | 387,350.00 USD | 731.87 USD | 0.00 USD | `+16.42%` | `5.03` |
| `Live` | `Short` | `147.50` | 471,390.00 USD | 84,040.00 USD | 0.00 USD | `+18.02%` | `569.76` |
| `Live` | `Short` | `148.50` | 473,910.00 USD | 2,520.00 USD | 0.00 USD | `+18.83%` | `16.98` |
| `Live` | `Short` | `150.50` | 474,080.00 USD | 167.06 USD | 0.00 USD | `+20.43%` | `1.11` |
| `Live` | `Short` | `151.50` | 474,320.00 USD | 237.85 USD | 0.00 USD | `+21.23%` | `1.57` |
| `Live` | `Short` | `152.50` | 1,070,000.00 USD | 594,420.00 USD | 0.00 USD | `+22.03%` | `3,897.82` |
| `Live` | `Short` | `154.50` | 1,100,000.00 USD | 32,450.00 USD | 0.00 USD | `+23.63%` | `210.00` |
| `Live` | `Short` | `155.50` | 1,100,000.00 USD | 1,900.00 USD | 0.00 USD | `+24.43%` | `12.22` |
| `Live` | `Short` | `158.50` | 1,100,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.83%` | `9.36` |
| `Live` | `Short` | `166.50` | 1,700,000.00 USD | 592,910.00 USD | 0.00 USD | `+33.23%` | `3,561.03` |
| `Live` | `Short` | `167.50` | 1,700,000.00 USD | 1,580.00 USD | 0.00 USD | `+34.03%` | `9.42` |
| `Live` | `Short` | `168.50` | 1,700,000.00 USD | 995.84 USD | 0.00 USD | `+34.83%` | `5.91` |
| `Live` | `Short` | `175.50` | 1,710,000.00 USD | 5,620.00 USD | 0.00 USD | `+40.43%` | `32.04` |
| `Live` | `Short` | `176.50` | 1,710,000.00 USD | 1,850.00 USD | 0.00 USD | `+41.23%` | `10.47` |
| `Live` | `Short` | `179.50` | 1,760,000.00 USD | 56,700.00 USD | 0.00 USD | `+43.63%` | `315.89` |
| `Live` | `Short` | `181.50` | 1,770,000.00 USD | 2,170.00 USD | 0.00 USD | `+45.23%` | `11.93` |
| `Live` | `Short` | `183.50` | 1,770,000.00 USD | 141.30 USD | 0.00 USD | `+46.83%` | `0.77` |
| `Live` | `Short` | `184.50` | 1,770,000.00 USD | 959.40 USD | 0.00 USD | `+47.63%` | `5.20` |
| `Live` | `Short` | `187.50` | 1,770,000.00 USD | 4,230.00 USD | 0.00 USD | `+50.03%` | `22.56` |
| `Live` | `Short` | `188.50` | 6,110,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+50.83%` | `23,000.00` |
| `Live` | `Short` | `189.50` | 6,140,000.00 USD | 34,730.00 USD | 0.00 USD | `+51.63%` | `183.28` |
| `Live` | `Short` | `191.50` | 6,150,000.00 USD | 4,180.00 USD | 0.00 USD | `+53.23%` | `21.85` |
| `Live` | `Short` | `192.50` | 6,150,000.00 USD | 358.05 USD | 0.00 USD | `+54.03%` | `1.86` |
| `Live` | `Short` | `193.50` | 6,150,000.00 USD | 286.38 USD | 0.00 USD | `+54.83%` | `1.48` |
| `Live` | `Short` | `194.50` | 6,150,000.00 USD | 4,670.00 USD | 0.00 USD | `+55.63%` | `24.03` |
| `Live` | `Short` | `195.50` | 6,150,000.00 USD | 1,500.00 USD | 0.00 USD | `+56.43%` | `7.67` |
| `Live` | `Short` | `196.50` | 9,490,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+57.23%` | `17,000.00` |
| `Live` | `Short` | `198.50` | 9,530,000.00 USD | 40,660.00 USD | 0.00 USD | `+58.83%` | `204.83` |
| `Live` | `Short` | `200.50` | 9,550,000.00 USD | 11,800.00 USD | 0.00 USD | `+60.43%` | `58.86` |
| `Live` | `Short` | `201.50` | 9,570,000.00 USD | 20,150.00 USD | 0.00 USD | `+61.23%` | `100.00` |
| `Live` | `Short` | `203.50` | 9,570,000.00 USD | 372.41 USD | 0.00 USD | `+62.83%` | `1.83` |
| `Live` | `Short` | `205.50` | 9,660,000.00 USD | 91,230.00 USD | 0.00 USD | `+64.43%` | `443.92` |
| `Live` | `Short` | `209.50` | 9,670,000.00 USD | 15,080.00 USD | 0.00 USD | `+67.64%` | `72.00` |
| `Live` | `Short` | `210.50` | 9,670,000.00 USD | 151.56 USD | 0.00 USD | `+68.44%` | `0.72` |
| `Live` | `Short` | `211.50` | 9,700,000.00 USD | 25,380.00 USD | 0.00 USD | `+69.24%` | `120.00` |
| `Live` | `Short` | `217.50` | 9,710,000.00 USD | 8,920.00 USD | 0.00 USD | `+74.04%` | `41.00` |
| `Live` | `Short` | `220.50` | 9,710,000.00 USD | 2,000.00 USD | 0.00 USD | `+76.44%` | `9.06` |
| `Live` | `Short` | `221.50` | 9,710,000.00 USD | 1,110.00 USD | 0.00 USD | `+77.24%` | `5.01` |
| `Live` | `Short` | `223.50` | 9,760,000.00 USD | 47,810.00 USD | 0.00 USD | `+78.84%` | `213.92` |
| `Live` | `Short` | `227.50` | 9,830,000.00 USD | 68,250.00 USD | 0.00 USD | `+82.04%` | `300.00` |
| `Live` | `Short` | `232.50` | 9,830,000.00 USD | 2,330.00 USD | 0.00 USD | `+86.04%` | `10.00` |
| `Live` | `Short` | `234.50` | 9,830,000.00 USD | 192.29 USD | 0.00 USD | `+87.64%` | `0.82` |
| `Live` | `Short` | `239.50` | 9,830,000.00 USD | 5,050.00 USD | 0.00 USD | `+91.64%` | `21.09` |
| `Live` | `Short` | `240.50` | 9,830,000.00 USD | 382.39 USD | 0.00 USD | `+92.44%` | `1.59` |
| `Live` | `Short` | `241.50` | 10,250,000.00 USD | 419,350.00 USD | 0.00 USD | `+93.24%` | `1,736.44` |
| `Live` | `Short` | `242.50` | 10,250,000.00 USD | 647.48 USD | 0.00 USD | `+94.04%` | `2.67` |
| `Live` | `Short` | `244.50` | 10,260,000.00 USD | 845.97 USD | 0.00 USD | `+95.64%` | `3.46` |
| `Live` | `Short` | `249.50` | 10,260,000.00 USD | 132.24 USD | 0.00 USD | `+99.64%` | `0.53` |

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
  * Current Rate: `-964.12` | Last 24h: `22.55K` | Last 3d: `65.35K` | Last 7d: `109.24K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0002%` | **USDT OKX** | `-0.0012%` |
| **USDT Bybit** | `-0.0034%` | **USDT KuCoin** | `0.0018%` |
| **USDT MEXC** | `-0.0003%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0038%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `127.08` | `128.36` | `127.08` | `132.12` | `125.96` | 9,241,707.96 USD | 3,635,148.90 USD | 5,606,559.06 USD | -1,971,410.16 USD | `-21.33%` | `6B / 35S` |
| `5:00 UTC` | `125.01` | `125.79` | `125.01` | `127.83` | `123.85` | 10,015,523.95 USD | 4,623,982.97 USD | 5,391,540.98 USD | -767,558.02 USD | `-7.66%` | `13B / 27S` |
| `0:00 UTC` | `125.93` | `126.72` | `125.93` | `128.21` | `125.19` | 5,502,618.32 USD | 2,933,878.59 USD | 2,568,739.72 USD | 365,138.87 USD | `+6.64%` | `24B / 11S` |
| `5:00 UTC` | `127.23` | `128.35` | `127.23` | `129.75` | `127.07` | 4,963,273.74 USD | 2,487,328.38 USD | 2,475,945.37 USD | 11,383.01 USD | `+0.23%` | `22B / 14S` |
| `0:00 UTC` | `126.01` | `127.30` | `126.01` | `128.37` | `125.73` | 4,752,146.34 USD | 1,764,767.19 USD | 2,987,379.15 USD | -1,222,611.96 USD | `-25.73%` | `19B / 40S` |
| `5:00 UTC` | `125.60` | `125.78` | `125.60` | `127.08` | `124.86` | 6,899,831.48 USD | 3,656,346.75 USD | 3,243,484.73 USD | 412,862.03 USD | `+5.98%` | `12B / 8S` |
| `0:00 UTC` | `124.36` | `124.46` | `124.36` | `125.78` | `123.48` | 7,451,122.63 USD | 3,127,709.63 USD | 4,323,413.00 USD | -1,195,703.37 USD | `-16.05%` | `4B / 21S` |
| `5:00 UTC` | `123.61` | `123.98` | `123.61` | `125.07` | `123.01` | 4,418,811.12 USD | 2,143,156.99 USD | 2,275,654.12 USD | -132,497.13 USD | `-3.00%` | `7B / 11S` |
| `0:00 UTC` | `123.51` | `123.74` | `123.51` | `125.27` | `122.59` | 9,249,156.63 USD | 3,934,205.15 USD | 5,314,951.48 USD | -1,380,746.33 USD | `-14.93%` | `1B / 29S` |
| `5:00 UTC` | `121.40` | `121.94` | `121.40` | `123.68` | `120.78` | 7,486,866.97 USD | 3,443,289.94 USD | 4,043,577.03 USD | -600,287.09 USD | `-8.02%` | `16B / 29S` |

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
| `5m` | -386,810.00 USD | -416,260.00 USD | **`DISTRIBUTION`** |
| `15m` | -797,920.00 USD | -3,090,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -833,980.00 USD | -3,670,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -940,130.00 USD | -5,430,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,280,000.00 USD | -5,120,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,090,000.00 USD | -10,070,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -6,850,000.00 USD | -10,990,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,530,000.00 USD | -11,270,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -6,790,000.00 USD | -12,880,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,760,000.00 USD | -11,260,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -28,830,000.00 USD | -49,420,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -117,490,000.00 USD | -112,480,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-386.81K` | 15m=`-797.92K` | 1h=`-940.13K` | 24h=`-7.76M`
* Futures Capital Netflows: 5m=`-416.26K` | 15m=`-3.09M` | 1h=`-5.43M` | 24h=`-11.26M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `121.68` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `118.71` (Risk Distance: `2.97` pts)
  * +2.5R Take Profit: `129.10`
  * Mathematical Lot Sizing: **`3.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `125.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `128.01` (Risk Distance: `2.97` pts)
  * +2.5R Take Profit: `117.62`
  * Mathematical Lot Sizing: **`3.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`121.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
