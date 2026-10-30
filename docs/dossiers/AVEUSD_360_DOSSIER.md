# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:27:10 IST` (`2026-10-30 09:57:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `124.33` | **Live Ask Quote**: `124.62` | **Mid Price**: `124.47`
- **Spread Points**: `29.00` | **Spread BPS**: `23.30 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `122.11` | VWAP Z-Score: `+0.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.03` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.83` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `131.91` | Lower -3.00σ Band: `112.31`
  * Upper +2.51σ Band: `130.31` | Lower -2.51σ Band: `113.91`
  * Upper +2.01σ Band: `128.67` | Lower -2.01σ Band: `115.54`
  * Upper +2.00σ Band: `128.64` | Lower -2.00σ Band: `115.57`
  * Upper +1.28σ Band: `126.29` | Lower -1.28σ Band: `117.93`
  * Upper +1.00σ Band: `125.37` | Lower -1.00σ Band: `118.84`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`124.63` | EMA-20=`124.64` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`124.93` (Slope: `+0.0000`) | EMA-100=`126.64`
  * Institutional Anchors: EMA-144=`127.77` | EMA-200=`128.82` (Slope: `-0.3855`) | EMA-233=`129.17`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `127.07` (Distance: `-2.06%`)
  * Point of Control (POC) = `124.41` (Distance: `+0.03%`)
  * Value Area Low (VAL) = `119.70` (Distance: `+3.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.33` | Weekly POC=`135.06` | Weekly VAL=`130.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`127.41` | Low=`123.78`
  * New York Session (13:00-21:00 UTC): High=`125.22` | Low=`123.73`
  * Initial Balance (First Hour): IB High=`126.87` | IB Low=`123.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `123.98` - `124.97`
  * Optimal Trade Entry (OTE 0.705): `124.72`
  * Structural Invalidation Anchor (0.786): `125.47`

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
| --- | **`124.47`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `411` | `0x3ee5...4fab` | `LONG` | 5,393,492.03 USD | `43,303.83` | `77.35` | `124.62` | `72.02` | 2,043,801.99 USD | `+37.89%` | `10X Cross` |
| `761` | `0xecb6...2b00` | `SHORT` | 2,998,428.36 USD | `24,077.96` | `133.17` | `124.62` | `1376.77` | 208,095.90 USD | `+6.94%` | `10X Cross` |
| `794` | `0x0514...bdfe` | `SHORT` | 2,864,190.00 USD | `23,000.00` | `87.41` | `124.62` | `155.47` | -853,710.78 USD | `-29.81%` | `10X Cross` |
| `832` | `0x08c1...1135` | `LONG` | 2,719,696.22 USD | `21,836.18` | `80.89` | `124.62` | `86.99` | 953,361.87 USD | `+35.05%` | `10X Cross` |
| `1023` | `0x0996...0ba6` | `SHORT` | 2,117,520.00 USD | `17,000.00` | `107.97` | `124.62` | `196.59` | -281,946.70 USD | `-13.31%` | `3X Cross` |
| `1110` | `0x45d2...4029` | `SHORT` | 1,958,522.18 USD | `15,721.00` | `118.40` | `124.62` | `2757.52` | -97,131.00 USD | `-4.96%` | `10X Cross` |
| `1128` | `0xbfc7...80b4` | `SHORT` | 1,938,649.18 USD | `15,561.48` | `115.30` | `124.62` | `224.10` | -144,349.86 USD | `-7.45%` | `10X Cross` |
| `1166` | `0x6540...f7b7` | `LONG` | 1,888,122.02 USD | `15,155.90` | `144.34` | `124.62` | `76.49` | -299,469.34 USD | `-15.86%` | `5X Isolated` |
| `1231` | `0x07fd...689d` | `LONG` | 1,784,854.87 USD | `14,332.73` | `148.42` | `124.62` | `0.000000` | -342,427.40 USD | `-19.19%` | `10X Cross` |
| `1452` | `0xcac1...26b3` | `SHORT` | 1,494,360.00 USD | `12,000.00` | `125.37` | `124.62` | `842.74` | 10,080.86 USD | `+0.67%` | `10X Cross` |
| `1454` | `0x12d2...f97f` | `LONG` | 1,490,032.84 USD | `11,961.41` | `133.88` | `124.62` | `0.000000` | -111,371.60 USD | `-7.47%` | `10X Cross` |
| `1461` | `0xeadc...9d55` | `LONG` | 1,473,023.95 USD | `11,823.92` | `89.93` | `124.62` | `0.000000` | 409,667.54 USD | `+27.81%` | `10X Cross` |
| `1634` | `0x9df2...c665` | `SHORT` | 1,292,746.37 USD | `10,380.17` | `133.78` | `124.62` | `3060.48` | 95,962.90 USD | `+7.42%` | `10X Cross` |
| `1690` | `0x3dc9...54b0` | `SHORT` | 1,245,700.00 USD | `10,000.00` | `128.60` | `124.62` | `1831.13` | 40,321.83 USD | `+3.24%` | `10X Cross` |
| `1816` | `0x8af7...fa05` | `SHORT` | 1,137,971.17 USD | `9,133.75` | `131.49` | `124.62` | `2195.48` | 63,009.57 USD | `+5.54%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `128.44` | 10,728.59 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 10.73K USD at 128.4400 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `128.74` | 370.77 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 0.37K USD at 128.7400 USD [API] | `2026-10-29 02:35:59` |
| `ANNOUNCEMENT` | `INFO` | `128.43` | 8,476.38 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 8.48K USD at 128.4300 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `128.48` | 2,998.72 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 3.00K USD at 128.4800 USD [API] | `2026-10-29 02:36:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`128.80` (Vol: 368,100.00 USD, Dist: `+3.44%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.43%`)
  * 48H Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+3.46%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.43%`)
  * 3D Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+3.46%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.43%`)
  * 7D Horizon: Short MP=`128.71` (Vol: 394,000.00 USD, Dist: `+3.37%`) | Long MP=`116.45` (Vol: 253,400.00 USD, Dist: `--6.48%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `25.50` | 188.96 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 265.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 5,950.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 118,170.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 303.78 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 483.52 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 7,630.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 21,820.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 1,620.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 424.50 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 487.21 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 2,760.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 45,520.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 555.39 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 617.11 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 6,690.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 27,320.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 848.12 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 64,170.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 506.87 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 4,270.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 5,550.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 101.08 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,260.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 23,780.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 1,860.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 8,820.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 3,150,000.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,400.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,890.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,160,000.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 14,680.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 3,670.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 3,800.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 5,500.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 54,210.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 15,760.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,930,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 60,610.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,230.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,650.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,750.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 19,120.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 4,190.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 9,350.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 95,290.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 37,380.00 USD | 946,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 27,360.00 USD | 909,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 68,140.00 USD | 881,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 18,880.00 USD | 813,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 24,400.00 USD | 794,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 36,040.00 USD | 770,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 86,270.00 USD | 734,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 25,870.00 USD | 648,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 10,530.00 USD | 622,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 34,850.00 USD | 611,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 8,410.00 USD | 576,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,400.00 USD | 568,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 436,940.00 USD | 566,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 16,160.00 USD | 129,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 113,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 49,760.00 USD | 79,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 29,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,770.00 USD | 24,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 8,970.00 USD | 22,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 195.05 USD | 13,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 173.01 USD | 173.01 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 5,400.00 USD | 12,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 6,480.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 17,260.00 USD | 17,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 30,110.00 USD | 47,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 33,820.00 USD | 81,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 297.70 USD | 81,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 258.24 USD | 81,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 252.53 USD | 82,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 2,850.00 USD | 85,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 87,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 719.82 USD | 88,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 89,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 108,770.00 USD | 198,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,530.00 USD | 201,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 606,040.00 USD | 807,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 14,600.00 USD | 821,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,280.00 USD | 823,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 1,990.00 USD | 825,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 457.53 USD | 826,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 10,160.00 USD | 836,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 3,580,000.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 6,180.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 159.88 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 874.72 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 4,260.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 50,250.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 1,540.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 1,070.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 19,160.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 319,360.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 1,550.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 33,330.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 538.18 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 16,590.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 1,500.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 5,440.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 1,050.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `206.50` | 39,650.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `215.50` | 8,840.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 1,130.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `224.50` | 3,490,000.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 67,950.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 61,360.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `228.50` | 249.07 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `229.50` | 1,030,000.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `231.50` | 2,310.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 386.37 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 2,120.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 409.82 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `244.50` | 163,310.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `249.50` | 3,940.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `250.50` | 51,310.00 USD | 14,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 8,200,000.00 USD | 0.00 USD | 188.96 USD | `-79.61%` | `7.41` |
| `Live` | `Long` | `26.50` | 8,200,000.00 USD | 0.00 USD | 265.00 USD | `-78.81%` | `10.00` |
| `Live` | `Long` | `27.50` | 8,200,000.00 USD | 0.00 USD | 5,950.00 USD | `-78.01%` | `216.36` |
| `Live` | `Long` | `29.50` | 8,190,000.00 USD | 0.00 USD | 118,170.00 USD | `-76.41%` | `4,005.60` |
| `Live` | `Long` | `30.50` | 8,070,000.00 USD | 0.00 USD | 303.78 USD | `-75.61%` | `9.96` |
| `Live` | `Long` | `31.50` | 8,070,000.00 USD | 0.00 USD | 483.52 USD | `-74.81%` | `15.35` |
| `Live` | `Long` | `32.50` | 8,070,000.00 USD | 0.00 USD | 7,630.00 USD | `-74.01%` | `234.90` |
| `Live` | `Long` | `34.50` | 8,070,000.00 USD | 0.00 USD | 21,820.00 USD | `-72.42%` | `632.60` |
| `Live` | `Long` | `35.50` | 8,040,000.00 USD | 0.00 USD | 1,620.00 USD | `-71.62%` | `45.73` |
| `Live` | `Long` | `37.50` | 8,040,000.00 USD | 0.00 USD | 424.50 USD | `-70.02%` | `11.32` |
| `Live` | `Long` | `38.50` | 8,040,000.00 USD | 0.00 USD | 232.54 USD | `-69.22%` | `6.04` |
| `Live` | `Long` | `40.50` | 8,040,000.00 USD | 0.00 USD | 487.21 USD | `-67.62%` | `12.03` |
| `Live` | `Long` | `44.50` | 8,040,000.00 USD | 0.00 USD | 2,760.00 USD | `-64.42%` | `62.13` |
| `Live` | `Long` | `48.50` | 8,040,000.00 USD | 0.00 USD | 45,520.00 USD | `-61.22%` | `938.50` |
| `Live` | `Long` | `49.50` | 7,990,000.00 USD | 0.00 USD | 555.39 USD | `-60.42%` | `11.22` |
| `Live` | `Long` | `50.50` | 7,990,000.00 USD | 0.00 USD | 617.11 USD | `-59.62%` | `12.22` |
| `Live` | `Long` | `53.50` | 7,990,000.00 USD | 0.00 USD | 6,690.00 USD | `-57.22%` | `125.00` |
| `Live` | `Long` | `54.50` | 7,980,000.00 USD | 0.00 USD | 27,320.00 USD | `-56.42%` | `501.34` |
| `Live` | `Long` | `56.50` | 7,960,000.00 USD | 0.00 USD | 1,510.00 USD | `-54.83%` | `26.66` |
| `Live` | `Long` | `57.50` | 7,960,000.00 USD | 0.00 USD | 848.12 USD | `-54.03%` | `14.75` |
| `Live` | `Long` | `58.50` | 7,950,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.23%` | `27.49` |
| `Live` | `Long` | `59.50` | 7,950,000.00 USD | 0.00 USD | 64,170.00 USD | `-52.43%` | `1,078.45` |
| `Live` | `Long` | `60.50` | 7,890,000.00 USD | 0.00 USD | 1,690.00 USD | `-51.63%` | `27.87` |
| `Live` | `Long` | `61.50` | 7,890,000.00 USD | 0.00 USD | 168.51 USD | `-50.83%` | `2.74` |
| `Live` | `Long` | `62.50` | 7,890,000.00 USD | 0.00 USD | 506.87 USD | `-50.03%` | `8.11` |
| `Live` | `Long` | `63.50` | 7,890,000.00 USD | 0.00 USD | 4,270.00 USD | `-49.23%` | `67.25` |
| `Live` | `Long` | `65.50` | 7,880,000.00 USD | 0.00 USD | 5,550.00 USD | `-47.63%` | `84.72` |
| `Live` | `Long` | `66.50` | 7,880,000.00 USD | 0.00 USD | 101.08 USD | `-46.83%` | `1.52` |
| `Live` | `Long` | `67.50` | 7,880,000.00 USD | 0.00 USD | 24,320.00 USD | `-46.03%` | `360.30` |
| `Live` | `Long` | `68.50` | 7,850,000.00 USD | 0.00 USD | 7,260.00 USD | `-45.23%` | `105.95` |
| `Live` | `Long` | `69.50` | 7,850,000.00 USD | 0.00 USD | 23,780.00 USD | `-44.43%` | `342.17` |
| `Live` | `Long` | `70.50` | 7,820,000.00 USD | 0.00 USD | 1,860.00 USD | `-43.63%` | `26.34` |
| `Live` | `Long` | `71.50` | 7,820,000.00 USD | 0.00 USD | 8,820.00 USD | `-42.83%` | `123.38` |
| `Live` | `Long` | `72.50` | 7,810,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-42.03%` | `43,411.83` |
| `Live` | `Long` | `73.50` | 4,660,000.00 USD | 0.00 USD | 11,400.00 USD | `-41.23%` | `155.11` |
| `Live` | `Long` | `74.50` | 4,650,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.43%` | `14.20` |
| `Live` | `Long` | `75.50` | 4,650,000.00 USD | 0.00 USD | 1,890.00 USD | `-39.63%` | `25.00` |
| `Live` | `Long` | `76.50` | 4,650,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-38.83%` | `15,161.00` |
| `Live` | `Long` | `77.50` | 3,490,000.00 USD | 0.00 USD | 9,050.00 USD | `-38.03%` | `116.79` |
| `Live` | `Long` | `78.50` | 3,480,000.00 USD | 0.00 USD | 14,680.00 USD | `-37.24%` | `187.03` |
| `Live` | `Long` | `79.50` | 3,470,000.00 USD | 0.00 USD | 6,790.00 USD | `-36.44%` | `85.43` |
| `Live` | `Long` | `80.50` | 3,460,000.00 USD | 0.00 USD | 3,670.00 USD | `-35.64%` | `45.64` |
| `Live` | `Long` | `82.50` | 3,450,000.00 USD | 0.00 USD | 3,800.00 USD | `-34.04%` | `46.11` |
| `Live` | `Long` | `83.50` | 3,450,000.00 USD | 0.00 USD | 5,500.00 USD | `-33.24%` | `65.91` |
| `Live` | `Long` | `85.50` | 3,450,000.00 USD | 0.00 USD | 54,210.00 USD | `-31.64%` | `634.00` |
| `Live` | `Long` | `86.50` | 3,390,000.00 USD | 0.00 USD | 15,760.00 USD | `-30.84%` | `182.18` |
| `Live` | `Long` | `87.50` | 3,380,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-30.04%` | `22,041.98` |
| `Live` | `Long` | `88.50` | 1,450,000.00 USD | 0.00 USD | 2,050.00 USD | `-29.24%` | `23.18` |
| `Live` | `Long` | `89.50` | 1,440,000.00 USD | 0.00 USD | 60,610.00 USD | `-28.44%` | `677.21` |
| `Live` | `Long` | `90.50` | 1,380,000.00 USD | 0.00 USD | 6,230.00 USD | `-27.64%` | `68.83` |
| `Live` | `Long` | `91.50` | 1,380,000.00 USD | 0.00 USD | 277,650.00 USD | `-26.84%` | `3,034.48` |
| `Live` | `Long` | `92.50` | 1,100,000.00 USD | 0.00 USD | 14,750.00 USD | `-26.04%` | `159.47` |
| `Live` | `Long` | `93.50` | 1,090,000.00 USD | 0.00 USD | 10,990.00 USD | `-25.24%` | `117.52` |
| `Live` | `Long` | `94.50` | 1,070,000.00 USD | 0.00 USD | 19,120.00 USD | `-24.44%` | `202.34` |
| `Live` | `Long` | `95.50` | 1,060,000.00 USD | 0.00 USD | 4,190.00 USD | `-23.64%` | `43.83` |
| `Live` | `Long` | `96.50` | 1,050,000.00 USD | 0.00 USD | 9,350.00 USD | `-22.84%` | `96.87` |
| `Live` | `Long` | `97.50` | 1,040,000.00 USD | 0.00 USD | 95,290.00 USD | `-22.04%` | `977.30` |
| `Live` | `Long` | `98.50` | 946,710.00 USD | 0.00 USD | 37,380.00 USD | `-21.24%` | `379.53` |
| `Live` | `Long` | `99.50` | 909,330.00 USD | 0.00 USD | 27,360.00 USD | `-20.44%` | `274.96` |
| `Live` | `Long` | `100.50` | 881,970.00 USD | 0.00 USD | 68,140.00 USD | `-19.64%` | `678.00` |
| `Live` | `Long` | `101.50` | 813,830.00 USD | 0.00 USD | 18,880.00 USD | `-18.85%` | `186.04` |
| `Live` | `Long` | `102.50` | 794,950.00 USD | 0.00 USD | 24,400.00 USD | `-18.05%` | `238.04` |
| `Live` | `Long` | `103.50` | 770,550.00 USD | 0.00 USD | 36,040.00 USD | `-17.25%` | `348.24` |
| `Live` | `Long` | `104.50` | 734,500.00 USD | 0.00 USD | 86,270.00 USD | `-16.45%` | `825.55` |
| `Live` | `Long` | `105.50` | 648,230.00 USD | 0.00 USD | 25,870.00 USD | `-15.65%` | `245.20` |
| `Live` | `Long` | `106.50` | 622,370.00 USD | 0.00 USD | 10,530.00 USD | `-14.85%` | `98.84` |
| `Live` | `Long` | `107.50` | 611,840.00 USD | 0.00 USD | 34,850.00 USD | `-14.05%` | `324.23` |
| `Live` | `Long` | `108.50` | 576,980.00 USD | 0.00 USD | 8,410.00 USD | `-13.25%` | `77.49` |
| `Live` | `Long` | `109.50` | 568,580.00 USD | 0.00 USD | 2,400.00 USD | `-12.45%` | `21.88` |
| `Live` | `Long` | `110.50` | 566,180.00 USD | 0.00 USD | 436,940.00 USD | `-11.65%` | `3,954.17` |
| `Live` | `Long` | `111.50` | 129,240.00 USD | 0.00 USD | 16,160.00 USD | `-10.85%` | `144.95` |
| `Live` | `Long` | `112.50` | 113,080.00 USD | 0.00 USD | 33,900.00 USD | `-10.05%` | `301.33` |
| `Live` | `Long` | `113.50` | 79,180.00 USD | 0.00 USD | 49,760.00 USD | `-9.25%` | `438.42` |
| `Live` | `Long` | `114.50` | 29,420.00 USD | 0.00 USD | 4,560.00 USD | `-8.45%` | `39.82` |
| `Live` | `Long` | `115.50` | 24,860.00 USD | 0.00 USD | 2,770.00 USD | `-7.65%` | `24.00` |
| `Live` | `Long` | `116.50` | 22,090.00 USD | 0.00 USD | 8,970.00 USD | `-6.85%` | `77.00` |
| `Live` | `Long` | `117.50` | 13,120.00 USD | 0.00 USD | 195.05 USD | `-6.05%` | `1.66` |
| `Live` | `Short` | `118.50` | 173.01 USD | 173.01 USD | 0.00 USD | `-5.25%` | `1.46` |
| `Live` | `Long` | `119.50` | 12,930.00 USD | 0.00 USD | 5,400.00 USD | `-4.45%` | `45.22` |
| `Live` | `Long` | `120.50` | 7,520.00 USD | 0.00 USD | 6,480.00 USD | `-3.65%` | `53.77` |
| `Live` | `Long` | `121.50` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-2.85%` | `8.58` |
| `Live` | `Short` | `130.50` | 17,430.00 USD | 17,260.00 USD | 0.00 USD | `+4.34%` | `132.25` |
| `Live` | `Short` | `131.50` | 47,550.00 USD | 30,110.00 USD | 0.00 USD | `+5.14%` | `229.01` |
| `Live` | `Short` | `132.50` | 81,370.00 USD | 33,820.00 USD | 0.00 USD | `+5.94%` | `255.25` |
| `Live` | `Short` | `133.50` | 81,660.00 USD | 297.70 USD | 0.00 USD | `+6.74%` | `2.23` |
| `Live` | `Short` | `134.50` | 81,920.00 USD | 258.24 USD | 0.00 USD | `+7.54%` | `1.92` |
| `Live` | `Short` | `136.50` | 82,180.00 USD | 252.53 USD | 0.00 USD | `+9.14%` | `1.85` |
| `Live` | `Short` | `137.50` | 85,030.00 USD | 2,850.00 USD | 0.00 USD | `+9.94%` | `20.75` |
| `Live` | `Short` | `138.50` | 87,880.00 USD | 2,850.00 USD | 0.00 USD | `+10.74%` | `20.56` |
| `Live` | `Short` | `139.50` | 88,600.00 USD | 719.82 USD | 0.00 USD | `+11.54%` | `5.16` |
| `Live` | `Short` | `140.50` | 89,750.00 USD | 1,150.00 USD | 0.00 USD | `+12.34%` | `8.19` |
| `Live` | `Short` | `141.50` | 198,520.00 USD | 108,770.00 USD | 0.00 USD | `+13.14%` | `768.71` |
| `Live` | `Short` | `142.50` | 201,050.00 USD | 2,530.00 USD | 0.00 USD | `+13.94%` | `17.73` |
| `Live` | `Short` | `143.50` | 807,090.00 USD | 606,040.00 USD | 0.00 USD | `+14.74%` | `4,223.30` |
| `Live` | `Short` | `144.50` | 821,690.00 USD | 14,600.00 USD | 0.00 USD | `+15.54%` | `101.04` |
| `Live` | `Short` | `148.50` | 823,970.00 USD | 2,280.00 USD | 0.00 USD | `+18.73%` | `15.36` |
| `Live` | `Short` | `150.50` | 825,960.00 USD | 1,990.00 USD | 0.00 USD | `+20.33%` | `13.23` |
| `Live` | `Short` | `151.50` | 826,420.00 USD | 457.53 USD | 0.00 USD | `+21.13%` | `3.02` |
| `Live` | `Short` | `154.50` | 836,580.00 USD | 10,160.00 USD | 0.00 USD | `+23.53%` | `65.78` |
| `Live` | `Short` | `155.50` | 4,420,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+24.33%` | `23,014.13` |
| `Live` | `Short` | `158.50` | 4,420,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.73%` | `9.36` |
| `Live` | `Short` | `160.50` | 4,420,000.00 USD | 6,180.00 USD | 0.00 USD | `+28.33%` | `38.53` |
| `Live` | `Short` | `161.50` | 4,420,000.00 USD | 159.88 USD | 0.00 USD | `+29.13%` | `0.99` |
| `Live` | `Short` | `163.50` | 4,420,000.00 USD | 874.72 USD | 0.00 USD | `+30.73%` | `5.35` |
| `Live` | `Short` | `164.50` | 4,430,000.00 USD | 4,260.00 USD | 0.00 USD | `+31.53%` | `25.90` |
| `Live` | `Short` | `167.50` | 4,480,000.00 USD | 50,250.00 USD | 0.00 USD | `+33.93%` | `300.00` |
| `Live` | `Short` | `171.50` | 4,480,000.00 USD | 1,540.00 USD | 0.00 USD | `+37.12%` | `9.00` |
| `Live` | `Short` | `172.50` | 4,480,000.00 USD | 1,070.00 USD | 0.00 USD | `+37.92%` | `6.20` |
| `Live` | `Short` | `175.50` | 4,500,000.00 USD | 19,160.00 USD | 0.00 USD | `+40.32%` | `109.17` |
| `Live` | `Short` | `181.50` | 4,500,000.00 USD | 2,170.00 USD | 0.00 USD | `+45.12%` | `11.93` |
| `Live` | `Short` | `182.50` | 4,820,000.00 USD | 319,360.00 USD | 0.00 USD | `+45.92%` | `1,749.91` |
| `Live` | `Short` | `183.50` | 4,820,000.00 USD | 141.30 USD | 0.00 USD | `+46.72%` | `0.77` |
| `Live` | `Short` | `185.50` | 4,820,000.00 USD | 1,550.00 USD | 0.00 USD | `+48.32%` | `8.36` |
| `Live` | `Short` | `186.50` | 4,860,000.00 USD | 33,330.00 USD | 0.00 USD | `+49.12%` | `178.70` |
| `Live` | `Short` | `187.50` | 4,860,000.00 USD | 4,230.00 USD | 0.00 USD | `+49.92%` | `22.56` |
| `Live` | `Short` | `189.50` | 4,860,000.00 USD | 538.18 USD | 0.00 USD | `+51.52%` | `2.84` |
| `Live` | `Short` | `194.50` | 4,880,000.00 USD | 16,590.00 USD | 0.00 USD | `+55.51%` | `85.28` |
| `Live` | `Short` | `195.50` | 4,880,000.00 USD | 1,500.00 USD | 0.00 USD | `+56.31%` | `7.67` |
| `Live` | `Short` | `196.50` | 8,220,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+57.11%` | `17,000.00` |
| `Live` | `Short` | `200.50` | 8,230,000.00 USD | 9,850.00 USD | 0.00 USD | `+60.31%` | `49.15` |
| `Live` | `Short` | `201.50` | 8,240,000.00 USD | 5,440.00 USD | 0.00 USD | `+61.11%` | `27.00` |
| `Live` | `Short` | `203.50` | 8,240,000.00 USD | 1,050.00 USD | 0.00 USD | `+62.71%` | `5.17` |
| `Live` | `Short` | `205.50` | 8,320,000.00 USD | 84,610.00 USD | 0.00 USD | `+64.31%` | `411.72` |
| `Live` | `Short` | `206.50` | 8,360,000.00 USD | 39,650.00 USD | 0.00 USD | `+65.11%` | `192.00` |
| `Live` | `Short` | `210.50` | 8,360,000.00 USD | 151.56 USD | 0.00 USD | `+68.31%` | `0.72` |
| `Live` | `Short` | `215.50` | 8,370,000.00 USD | 8,840.00 USD | 0.00 USD | `+72.30%` | `41.00` |
| `Live` | `Short` | `218.50` | 8,370,000.00 USD | 1,130.00 USD | 0.00 USD | `+74.70%` | `5.15` |
| `Live` | `Short` | `220.50` | 8,370,000.00 USD | 2,000.00 USD | 0.00 USD | `+76.30%` | `9.06` |
| `Live` | `Short` | `224.50` | 11,870,000.00 USD | 3,490,000.00 USD | 0.00 USD | `+79.50%` | `15,561.48` |
| `Live` | `Short` | `226.50` | 11,930,000.00 USD | 67,950.00 USD | 0.00 USD | `+81.10%` | `300.00` |
| `Live` | `Short` | `227.50` | 12,000,000.00 USD | 61,360.00 USD | 0.00 USD | `+81.90%` | `269.73` |
| `Live` | `Short` | `228.50` | 12,000,000.00 USD | 249.07 USD | 0.00 USD | `+82.70%` | `1.09` |
| `Live` | `Short` | `229.50` | 13,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+83.50%` | `4,508.67` |
| `Live` | `Short` | `231.50` | 13,030,000.00 USD | 2,310.00 USD | 0.00 USD | `+85.10%` | `10.00` |
| `Live` | `Short` | `232.50` | 13,850,000.00 USD | 818,270.00 USD | 0.00 USD | `+85.90%` | `3,519.45` |
| `Live` | `Short` | `238.50` | 13,850,000.00 USD | 386.37 USD | 0.00 USD | `+90.69%` | `1.62` |
| `Live` | `Short` | `240.50` | 13,850,000.00 USD | 2,120.00 USD | 0.00 USD | `+92.29%` | `8.82` |
| `Live` | `Short` | `242.50` | 13,850,000.00 USD | 409.82 USD | 0.00 USD | `+93.89%` | `1.69` |
| `Live` | `Short` | `244.50` | 14,020,000.00 USD | 163,310.00 USD | 0.00 USD | `+95.49%` | `667.95` |
| `Live` | `Short` | `249.50` | 14,020,000.00 USD | 3,940.00 USD | 0.00 USD | `+99.49%` | `15.81` |
| `Live` | `Short` | `250.50` | 14,070,000.00 USD | 51,310.00 USD | 0.00 USD | `+100.29%` | `204.83` |

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
  * Current Rate: `2.43K` | Last 24h: `2.78K` | Last 3d: `40.34K` | Last 7d: `111.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0001%` | **USDT OKX** | `-0.0029%` |
| **USDT Bybit** | `0.0066%` | **USDT KuCoin** | `0.0011%` |
| **USDT MEXC** | `0.0001%` | **USDT BingX** | `0.0076%` |
| **USDT Gate** | `0.0005%` | **USDT Bitget** | `0.0024%` |
| **CoinM Binance** | `0.1437%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `126.06` | `125.45` | `126.06` | `126.25` | `124.81` | 1,613,048.55 USD | 753,514.49 USD | 859,534.06 USD | -106,019.57 USD | `-6.57%` | `16B / 54S` |
| `5:00 UTC` | `125.06` | `125.16` | `125.06` | `125.59` | `124.80` | 1,451,895.08 USD | 700,314.65 USD | 751,580.42 USD | -51,265.77 USD | `-3.53%` | `14B / 12S` |
| `0:00 UTC` | `125.19` | `125.12` | `125.19` | `125.45` | `124.72` | 893,258.87 USD | 412,743.87 USD | 480,515.00 USD | -67,771.12 USD | `-7.59%` | `7B / 17S` |
| `5:00 UTC` | `125.34` | `125.36` | `125.34` | `125.68` | `125.05` | 944,493.33 USD | 470,610.76 USD | 473,882.56 USD | -3,271.80 USD | `-0.35%` | `9B / 6S` |
| `0:00 UTC` | `125.27` | `125.16` | `125.27` | `125.47` | `124.73` | 786,073.81 USD | 420,964.65 USD | 365,109.16 USD | 55,855.49 USD | `+7.11%` | `10B / 9S` |
| `5:00 UTC` | `125.00` | `125.10` | `125.00` | `125.53` | `124.66` | 887,277.31 USD | 387,796.46 USD | 499,480.85 USD | -111,684.39 USD | `-12.59%` | `10B / 23S` |
| `0:00 UTC` | `124.45` | `124.82` | `124.45` | `125.66` | `124.31` | 1,781,424.08 USD | 591,700.01 USD | 1,189,724.07 USD | -598,024.06 USD | `-33.57%` | `13B / 39S` |
| `5:00 UTC` | `124.41` | `124.42` | `124.41` | `124.69` | `124.20` | 1,280,426.88 USD | 695,542.34 USD | 584,884.54 USD | 110,657.80 USD | `+8.64%` | `8B / 5S` |
| `0:00 UTC` | `124.56` | `124.51` | `124.56` | `124.78` | `124.10` | 675,363.07 USD | 319,234.27 USD | 356,128.80 USD | -36,894.54 USD | `-5.46%` | `7B / 14S` |
| `5:00 UTC` | `124.98` | `124.67` | `124.98` | `125.03` | `124.30` | 541,745.99 USD | 228,045.95 USD | 313,700.05 USD | -85,654.10 USD | `-15.81%` | `9B / 9S` |

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
| `5m` | 0.00 USD | 16,420.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | -32,070.00 USD | **`DISTRIBUTION`** |
| `30m` | 0.00 USD | 370,520.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | -363,500.00 USD | **`DISTRIBUTION`** |
| `2h` | 0.00 USD | -726,540.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | 787,260.00 USD | **`ACCUMULATION`** |
| `6h` | 0.00 USD | 4,310,000.00 USD | **`ACCUMULATION`** |
| `8h` | 0.00 USD | 6,750,000.00 USD | **`ACCUMULATION`** |
| `12h` | 0.00 USD | -666,260.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -8,000,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -44,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -95,240,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+16.42K` | 15m=`-32.07K` | 1h=`-363.50K` | 24h=`-8.00M`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `119.70` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `118.03` (Risk Distance: `1.67` pts)
  * +2.5R Take Profit: `123.88`
  * Mathematical Lot Sizing: **`5.98 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `127.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `128.74` (Risk Distance: `1.67` pts)
  * +2.5R Take Profit: `122.89`
  * Mathematical Lot Sizing: **`5.98 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`125.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
