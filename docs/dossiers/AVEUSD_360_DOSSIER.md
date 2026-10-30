# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:36:47 IST` (`2026-10-30 11:06:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `126.01` | **Live Ask Quote**: `126.31` | **Mid Price**: `126.16`
- **Spread Points**: `30.00` | **Spread BPS**: `23.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `126.16` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `127.04` | Lower -3.00σ Band: `125.28`
  * Upper +2.51σ Band: `126.85` | Lower -2.51σ Band: `125.47`
  * Upper +2.01σ Band: `126.69` | Lower -2.01σ Band: `125.63`
  * Upper +2.00σ Band: `126.66` | Lower -2.00σ Band: `125.66`
  * Upper +1.28σ Band: `126.51` | Lower -1.28σ Band: `125.81`
  * Upper +1.00σ Band: `126.41` | Lower -1.00σ Band: `125.91`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`126.16` | EMA-20=`126.16` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`126.16` (Slope: `+0.0000`) | EMA-100=`126.16`
  * Institutional Anchors: EMA-144=`126.16` | EMA-200=`126.16` (Slope: `+0.0000`) | EMA-233=`126.16`
- **Range Boundaries**: 24H High=`127.42` | 24H Low=`124.90` | Weekly High=`128.68` | Weekly Low=`123.64`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `127.07` (Distance: `-0.71%`)
  * Point of Control (POC) = `124.41` (Distance: `+1.41%`)
  * Value Area Low (VAL) = `119.87` (Distance: `+5.25%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.49` | Weekly POC=`135.06` | Weekly VAL=`130.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`127.41` | Low=`123.78`
  * New York Session (13:00-21:00 UTC): High=`126.06` | Low=`123.86`
  * Initial Balance (First Hour): IB High=`126.87` | IB Low=`123.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `125.66` - `126.66`
  * Optimal Trade Entry (OTE 0.705): `126.41`
  * Structural Invalidation Anchor (0.786): `127.17`

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
| --- | **`126.16`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `408` | `0x3ee5...4fab` | `LONG` | 5,457,148.66 USD | `43,303.83` | `77.35` | `126.21` | `71.64` | 2,107,458.62 USD | `+38.62%` | `10X Cross` |
| `779` | `0xecb6...2b00` | `SHORT` | 2,929,630.57 USD | `23,210.51` | `133.17` | `126.21` | `1515.12` | 161,373.13 USD | `+5.51%` | `10X Cross` |
| `784` | `0x0514...bdfe` | `SHORT` | 2,898,915.40 USD | `23,000.00` | `87.41` | `126.21` | `155.41` | -888,436.18 USD | `-30.65%` | `10X Cross` |
| `823` | `0x08c1...1135` | `LONG` | 2,756,490.18 USD | `21,836.18` | `80.89` | `126.21` | `86.05` | 990,155.83 USD | `+35.92%` | `10X Cross` |
| `1014` | `0x0996...0ba6` | `SHORT` | 2,141,490.00 USD | `17,000.00` | `107.97` | `126.21` | `196.59` | -305,916.70 USD | `-14.29%` | `3X Cross` |
| `1093` | `0x45d2...4029` | `SHORT` | 1,983,754.39 USD | `15,721.00` | `118.40` | `126.21` | `2664.56` | -122,363.20 USD | `-6.17%` | `10X Cross` |
| `1108` | `0xbfc7...80b4` | `SHORT` | 1,964,247.81 USD | `15,561.48` | `115.30` | `126.21` | `217.86` | -169,948.49 USD | `-8.65%` | `10X Cross` |
| `1150` | `0x6540...f7b7` | `LONG` | 1,913,432.38 USD | `15,155.90` | `144.34` | `126.21` | `76.50` | -274,158.99 USD | `-14.33%` | `5X Isolated` |
| `1216` | `0x07fd...689d` | `LONG` | 1,810,080.47 USD | `14,332.73` | `148.42` | `126.21` | `0.000000` | -317,201.80 USD | `-17.52%` | `10X Cross` |
| `1440` | `0xcac1...26b3` | `SHORT` | 1,514,640.00 USD | `12,000.00` | `125.37` | `126.21` | `852.88` | -10,199.14 USD | `-0.67%` | `10X Cross` |
| `1445` | `0x12d2...f97f` | `LONG` | 1,506,659.20 USD | `11,961.41` | `133.88` | `126.21` | `0.000000` | -94,745.24 USD | `-6.29%` | `10X Cross` |
| `1452` | `0xeadc...9d55` | `LONG` | 1,492,651.66 USD | `11,823.92` | `89.93` | `126.21` | `0.000000` | 429,295.25 USD | `+28.76%` | `10X Cross` |
| `1619` | `0x9df2...c665` | `SHORT` | 1,305,715.32 USD | `10,352.96` | `133.78` | `126.21` | `2151.29` | 79,353.67 USD | `+6.08%` | `10X Cross` |
| `1670` | `0x3dc9...54b0` | `SHORT` | 1,261,400.00 USD | `10,000.00` | `128.60` | `126.21` | `1764.81` | 24,621.83 USD | `+1.95%` | `10X Cross` |
| `1801` | `0x8af7...fa05` | `SHORT` | 1,151,035.18 USD | `9,133.75` | `131.49` | `126.21` | `2176.88` | 49,945.57 USD | `+4.34%` | `10X Cross` |
| `1996` | `0x72db...8bb6` | `LONG` | 1,009,400.00 USD | `8,000.00` | `180.99` | `126.21` | `0.000000` | -438,557.43 USD | `-43.45%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`128.80` (Vol: 368,100.00 USD, Dist: `+3.50%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.37%`)
  * 48H Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+3.51%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.38%`)
  * 3D Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+3.51%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.38%`)
  * 7D Horizon: Short MP=`128.71` (Vol: 394,000.00 USD, Dist: `+3.42%`) | Long MP=`116.45` (Vol: 253,400.00 USD, Dist: `--6.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `26.50` | 3,720.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 5,740.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 114,210.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 165.20 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 231.80 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 1,800.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 529.57 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 8,350.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 24,150.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 158.94 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 356.70 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 2,760.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 46,500.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 293.03 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 471.87 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 27,320.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 6,940.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 2,470.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 66,930.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 661.74 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 506.87 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 4,270.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 434.27 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 101.08 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 29,330.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,110.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 23,930.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 8,140.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,410.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 3,140,000.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 19,810.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,890.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,160,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 9,510.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 14,400.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 6,780.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 44,800.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 1,900,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 14,820.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 15,120.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 60,720.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,460.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,420.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,750.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 19,350.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 4,300.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 9,050.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 95,290.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 38,060.00 USD | 974,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 10,680.00 USD | 936,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 18,550.00 USD | 926,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 18,880.00 USD | 907,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 24,400.00 USD | 888,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 36,040.00 USD | 864,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 87,240.00 USD | 828,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 100,380.00 USD | 741,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 10,530.00 USD | 640,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 34,850.00 USD | 630,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 7,660.00 USD | 595,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,400.00 USD | 587,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 436,940.00 USD | 585,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 16,160.00 USD | 148,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 132,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 49,760.00 USD | 98,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 48,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,770.00 USD | 43,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 8,970.00 USD | 41,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 14,610.00 USD | 32,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 437.27 USD | 17,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 15,310.00 USD | 17,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 806.14 USD | 1,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 28,270.00 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 35,000.00 USD | 76,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 3,090.00 USD | 80,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 162.75 USD | 80,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 252.53 USD | 80,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 2,850.00 USD | 83,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 86,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 719.82 USD | 86,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 88,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 108,770.00 USD | 196,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,730.00 USD | 199,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 607,480.00 USD | 807,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 150.28 USD | 807,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 14,550.00 USD | 821,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,280.00 USD | 824,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 1,990.00 USD | 826,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 457.53 USD | 826,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 3,580,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 874.72 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 162.85 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 4,310.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 50,250.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 103,960.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 20,530.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 1,600.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 322,490.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 1,150.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 33,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,630.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 538.18 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 16,590.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 1,500.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 15,270.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 124,060.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `206.50` | 689.71 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `214.50` | 8,790.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 3,570,000.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 67,950.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `229.50` | 1,030,000.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 251.25 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `231.50` | 2,310.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `237.50` | 384.75 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 162,760.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 409.82 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `246.50` | 50,490.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `247.50` | 3,910.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 8,160,000.00 USD | 0.00 USD | 209.10 USD | `-79.73%` | `8.20` |
| `Live` | `Long` | `26.50` | 8,160,000.00 USD | 0.00 USD | 1,200.00 USD | `-78.93%` | `45.35` |
| `Live` | `Long` | `27.50` | 8,160,000.00 USD | 0.00 USD | 11,110.00 USD | `-78.14%` | `403.91` |
| `Live` | `Long` | `30.50` | 8,150,000.00 USD | 0.00 USD | 122,470.00 USD | `-75.75%` | `4,015.35` |
| `Live` | `Long` | `31.50` | 8,030,000.00 USD | 0.00 USD | 19,930.00 USD | `-74.96%` | `632.60` |
| `Live` | `Long` | `32.50` | 8,010,000.00 USD | 0.00 USD | 691.60 USD | `-74.16%` | `21.28` |
| `Live` | `Long` | `34.50` | 8,000,000.00 USD | 0.00 USD | 132.13 USD | `-72.57%` | `3.83` |
| `Live` | `Long` | `35.50` | 8,000,000.00 USD | 0.00 USD | 1,620.00 USD | `-71.78%` | `45.73` |
| `Live` | `Long` | `38.50` | 8,000,000.00 USD | 0.00 USD | 232.54 USD | `-69.39%` | `6.04` |
| `Live` | `Long` | `39.50` | 8,000,000.00 USD | 0.00 USD | 36,980.00 USD | `-68.60%` | `936.21` |
| `Live` | `Long` | `44.50` | 7,970,000.00 USD | 0.00 USD | 2,760.00 USD | `-64.62%` | `62.13` |
| `Live` | `Long` | `45.50` | 7,960,000.00 USD | 0.00 USD | 5,690.00 USD | `-63.83%` | `125.00` |
| `Live` | `Long` | `46.50` | 7,960,000.00 USD | 0.00 USD | 158.10 USD | `-63.03%` | `3.40` |
| `Live` | `Long` | `49.50` | 7,960,000.00 USD | 0.00 USD | 158.40 USD | `-60.65%` | `3.20` |
| `Live` | `Long` | `50.50` | 7,960,000.00 USD | 0.00 USD | 445.41 USD | `-59.85%` | `8.82` |
| `Live` | `Long` | `51.50` | 7,960,000.00 USD | 0.00 USD | 1,780.00 USD | `-59.06%` | `34.61` |
| `Live` | `Long` | `53.50` | 7,950,000.00 USD | 0.00 USD | 122.52 USD | `-57.47%` | `2.29` |
| `Live` | `Long` | `54.50` | 7,950,000.00 USD | 0.00 USD | 59,580.00 USD | `-56.67%` | `1,093.23` |
| `Live` | `Long` | `55.50` | 7,890,000.00 USD | 0.00 USD | 27,000.00 USD | `-55.88%` | `486.56` |
| `Live` | `Long` | `56.50` | 7,870,000.00 USD | 0.00 USD | 2,340.00 USD | `-55.08%` | `41.41` |
| `Live` | `Long` | `58.50` | 7,870,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.49%` | `27.49` |
| `Live` | `Long` | `60.50` | 7,860,000.00 USD | 0.00 USD | 6,180.00 USD | `-51.90%` | `102.16` |
| `Live` | `Long` | `61.50` | 7,860,000.00 USD | 0.00 USD | 400.37 USD | `-51.11%` | `6.51` |
| `Live` | `Long` | `62.50` | 7,860,000.00 USD | 0.00 USD | 506.87 USD | `-50.31%` | `8.11` |
| `Live` | `Long` | `63.50` | 7,860,000.00 USD | 0.00 USD | 4,780.00 USD | `-49.52%` | `75.30` |
| `Live` | `Long` | `64.50` | 7,850,000.00 USD | 0.00 USD | 313.47 USD | `-48.72%` | `4.86` |
| `Live` | `Long` | `65.50` | 7,850,000.00 USD | 0.00 USD | 6,900.00 USD | `-47.92%` | `105.39` |
| `Live` | `Long` | `66.50` | 7,840,000.00 USD | 0.00 USD | 101.08 USD | `-47.13%` | `1.52` |
| `Live` | `Long` | `67.50` | 7,840,000.00 USD | 0.00 USD | 24,470.00 USD | `-46.33%` | `362.50` |
| `Live` | `Long` | `68.50` | 7,820,000.00 USD | 0.00 USD | 7,110.00 USD | `-45.54%` | `103.75` |
| `Live` | `Long` | `69.50` | 7,810,000.00 USD | 0.00 USD | 23,780.00 USD | `-44.74%` | `342.17` |
| `Live` | `Long` | `70.50` | 7,790,000.00 USD | 0.00 USD | 4,670.00 USD | `-43.95%` | `66.22` |
| `Live` | `Long` | `71.50` | 7,780,000.00 USD | 0.00 USD | 3,100,000.00 USD | `-43.15%` | `43,323.59` |
| `Live` | `Long` | `72.50` | 4,690,000.00 USD | 0.00 USD | 17,410.00 USD | `-42.36%` | `240.16` |
| `Live` | `Long` | `73.50` | 4,670,000.00 USD | 0.00 USD | 11,400.00 USD | `-41.56%` | `155.11` |
| `Live` | `Long` | `74.50` | 4,660,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.77%` | `14.20` |
| `Live` | `Long` | `75.50` | 4,660,000.00 USD | 0.00 USD | 1,890.00 USD | `-39.97%` | `25.00` |
| `Live` | `Long` | `76.50` | 4,660,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-39.18%` | `15,157.94` |
| `Live` | `Long` | `77.50` | 3,500,000.00 USD | 0.00 USD | 9,940.00 USD | `-38.38%` | `128.28` |
| `Live` | `Long` | `78.50` | 3,490,000.00 USD | 0.00 USD | 4,310.00 USD | `-37.59%` | `54.87` |
| `Live` | `Long` | `79.50` | 3,480,000.00 USD | 0.00 USD | 7,090.00 USD | `-36.79%` | `89.17` |
| `Live` | `Long` | `80.50` | 3,470,000.00 USD | 0.00 USD | 2,510.00 USD | `-36.00%` | `31.14` |
| `Live` | `Long` | `81.50` | 3,470,000.00 USD | 0.00 USD | 5,630.00 USD | `-35.20%` | `69.07` |
| `Live` | `Long` | `82.50` | 3,470,000.00 USD | 0.00 USD | 4,280.00 USD | `-34.41%` | `51.86` |
| `Live` | `Long` | `83.50` | 3,460,000.00 USD | 0.00 USD | 2,900.00 USD | `-33.61%` | `34.77` |
| `Live` | `Long` | `84.50` | 3,460,000.00 USD | 0.00 USD | 13,320.00 USD | `-32.82%` | `157.67` |
| `Live` | `Long` | `85.50` | 3,450,000.00 USD | 0.00 USD | 53,350.00 USD | `-32.02%` | `624.00` |
| `Live` | `Long` | `86.50` | 3,390,000.00 USD | 0.00 USD | 1,940,000.00 USD | `-31.23%` | `22,478.83` |
| `Live` | `Long` | `87.50` | 1,450,000.00 USD | 0.00 USD | 15,040.00 USD | `-30.43%` | `171.92` |
| `Live` | `Long` | `88.50` | 1,430,000.00 USD | 0.00 USD | 2,050.00 USD | `-29.64%` | `23.18` |
| `Live` | `Long` | `89.50` | 1,430,000.00 USD | 0.00 USD | 3,370.00 USD | `-28.84%` | `37.61` |
| `Live` | `Long` | `90.50` | 1,430,000.00 USD | 0.00 USD | 6,230.00 USD | `-28.05%` | `68.83` |
| `Live` | `Long` | `91.50` | 1,420,000.00 USD | 0.00 USD | 2,920.00 USD | `-27.25%` | `31.94` |
| `Live` | `Long` | `92.50` | 1,420,000.00 USD | 0.00 USD | 14,750.00 USD | `-26.46%` | `159.47` |
| `Live` | `Long` | `93.50` | 1,400,000.00 USD | 0.00 USD | 10,990.00 USD | `-25.66%` | `117.52` |
| `Live` | `Long` | `94.50` | 1,390,000.00 USD | 0.00 USD | 302,850.00 USD | `-24.87%` | `3,204.77` |
| `Live` | `Long` | `95.50` | 1,090,000.00 USD | 0.00 USD | 10,030.00 USD | `-24.07%` | `104.98` |
| `Live` | `Long` | `96.50` | 1,080,000.00 USD | 0.00 USD | 9,050.00 USD | `-23.28%` | `93.75` |
| `Live` | `Long` | `97.50` | 1,070,000.00 USD | 0.00 USD | 102,020.00 USD | `-22.48%` | `1,046.36` |
| `Live` | `Long` | `98.50` | 968,770.00 USD | 0.00 USD | 38,760.00 USD | `-21.69%` | `393.51` |
| `Live` | `Long` | `99.50` | 930,010.00 USD | 0.00 USD | 10,680.00 USD | `-20.89%` | `107.31` |
| `Live` | `Long` | `100.50` | 919,330.00 USD | 0.00 USD | 5,580.00 USD | `-20.10%` | `55.56` |
| `Live` | `Long` | `101.50` | 913,750.00 USD | 0.00 USD | 18,880.00 USD | `-19.30%` | `186.04` |
| `Live` | `Long` | `102.50` | 894,860.00 USD | 0.00 USD | 24,400.00 USD | `-18.51%` | `238.04` |
| `Live` | `Long` | `103.50` | 870,460.00 USD | 0.00 USD | 110,490.00 USD | `-17.71%` | `1,067.49` |
| `Live` | `Long` | `104.50` | 759,980.00 USD | 0.00 USD | 88,120.00 USD | `-16.92%` | `843.27` |
| `Live` | `Long` | `105.50` | 671,860.00 USD | 0.00 USD | 24,450.00 USD | `-16.12%` | `231.79` |
| `Live` | `Long` | `106.50` | 647,400.00 USD | 0.00 USD | 33,900.00 USD | `-15.33%` | `318.28` |
| `Live` | `Long` | `107.50` | 613,510.00 USD | 0.00 USD | 34,850.00 USD | `-14.53%` | `324.23` |
| `Live` | `Long` | `108.50` | 578,650.00 USD | 0.00 USD | 10,920.00 USD | `-13.74%` | `100.63` |
| `Live` | `Long` | `109.50` | 567,730.00 USD | 0.00 USD | 2,400.00 USD | `-12.94%` | `21.88` |
| `Live` | `Long` | `110.50` | 565,340.00 USD | 0.00 USD | 433,620.00 USD | `-12.15%` | `3,924.17` |
| `Live` | `Long` | `111.50` | 131,720.00 USD | 0.00 USD | 16,160.00 USD | `-11.35%` | `144.95` |
| `Live` | `Long` | `112.50` | 115,550.00 USD | 0.00 USD | 42,460.00 USD | `-10.56%` | `377.46` |
| `Live` | `Long` | `113.50` | 73,090.00 USD | 0.00 USD | 49,760.00 USD | `-9.76%` | `438.42` |
| `Live` | `Long` | `114.50` | 23,330.00 USD | 0.00 USD | 3,920.00 USD | `-8.97%` | `34.27` |
| `Live` | `Long` | `115.50` | 19,400.00 USD | 0.00 USD | 2,770.00 USD | `-8.17%` | `24.00` |
| `Live` | `Long` | `117.50` | 16,630.00 USD | 0.00 USD | 1,760.00 USD | `-6.58%` | `15.01` |
| `Live` | `Long` | `118.50` | 14,870.00 USD | 0.00 USD | 437.27 USD | `-5.79%` | `3.69` |
| `Live` | `Long` | `119.50` | 14,430.00 USD | 0.00 USD | 12,580.00 USD | `-4.99%` | `105.30` |
| `Live` | `Long` | `120.50` | 1,850.00 USD | 0.00 USD | 806.14 USD | `-4.20%` | `6.69` |
| `Live` | `Long` | `121.50` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-3.40%` | `8.58` |
| `Live` | `Short` | `122.50` | 2,820.00 USD | 2,820.00 USD | 0.00 USD | `-2.61%` | `23.03` |
| `Live` | `Short` | `124.50` | 3,670.00 USD | 846.60 USD | 0.00 USD | `-1.02%` | `6.80` |
| `Live` | `Short` | `130.50` | 16,300.00 USD | 12,640.00 USD | 0.00 USD | `+3.75%` | `96.83` |
| `Live` | `Short` | `131.50` | 44,730.00 USD | 28,430.00 USD | 0.00 USD | `+4.55%` | `216.18` |
| `Live` | `Short` | `132.50` | 79,730.00 USD | 35,000.00 USD | 0.00 USD | `+5.34%` | `264.17` |
| `Live` | `Short` | `133.50` | 80,320.00 USD | 583.39 USD | 0.00 USD | `+6.14%` | `4.37` |
| `Live` | `Short` | `134.50` | 80,480.00 USD | 162.75 USD | 0.00 USD | `+6.93%` | `1.21` |
| `Live` | `Short` | `135.50` | 81,690.00 USD | 1,210.00 USD | 0.00 USD | `+7.73%` | `8.92` |
| `Live` | `Short` | `136.50` | 81,940.00 USD | 252.53 USD | 0.00 USD | `+8.52%` | `1.85` |
| `Live` | `Short` | `137.50` | 84,790.00 USD | 2,850.00 USD | 0.00 USD | `+9.32%` | `20.75` |
| `Live` | `Short` | `138.50` | 89,380.00 USD | 4,590.00 USD | 0.00 USD | `+10.11%` | `33.11` |
| `Live` | `Short` | `139.50` | 90,100.00 USD | 719.82 USD | 0.00 USD | `+10.91%` | `5.16` |
| `Live` | `Short` | `141.50` | 198,870.00 USD | 108,770.00 USD | 0.00 USD | `+12.50%` | `768.71` |
| `Live` | `Short` | `142.50` | 201,610.00 USD | 2,730.00 USD | 0.00 USD | `+13.29%` | `19.19` |
| `Live` | `Short` | `143.50` | 822,440.00 USD | 620,830.00 USD | 0.00 USD | `+14.09%` | `4,326.35` |
| `Live` | `Short` | `144.50` | 822,590.00 USD | 150.28 USD | 0.00 USD | `+14.88%` | `1.04` |
| `Live` | `Short` | `148.50` | 824,870.00 USD | 2,280.00 USD | 0.00 USD | `+18.06%` | `15.36` |
| `Live` | `Short` | `150.50` | 825,790.00 USD | 919.56 USD | 0.00 USD | `+19.65%` | `6.11` |
| `Live` | `Short` | `151.50` | 826,250.00 USD | 457.53 USD | 0.00 USD | `+20.45%` | `3.02` |
| `Live` | `Short` | `155.50` | 4,400,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+23.63%` | `23,014.13` |
| `Live` | `Short` | `158.50` | 4,410,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.01%` | `9.36` |
| `Live` | `Short` | `159.50` | 4,410,000.00 USD | 157.91 USD | 0.00 USD | `+26.81%` | `0.99` |
| `Live` | `Short` | `163.50` | 4,410,000.00 USD | 874.72 USD | 0.00 USD | `+29.99%` | `5.35` |
| `Live` | `Short` | `166.50` | 4,410,000.00 USD | 1,030.00 USD | 0.00 USD | `+32.37%` | `6.20` |
| `Live` | `Short` | `167.50` | 4,460,000.00 USD | 50,250.00 USD | 0.00 USD | `+33.17%` | `300.00` |
| `Live` | `Short` | `170.50` | 4,460,000.00 USD | 1,530.00 USD | 0.00 USD | `+35.55%` | `9.00` |
| `Live` | `Short` | `172.50` | 4,460,000.00 USD | 201.82 USD | 0.00 USD | `+37.14%` | `1.17` |
| `Live` | `Short` | `175.50` | 4,470,000.00 USD | 5,970.00 USD | 0.00 USD | `+39.53%` | `34.01` |
| `Live` | `Short` | `176.50` | 4,480,000.00 USD | 13,410.00 USD | 0.00 USD | `+40.32%` | `75.96` |
| `Live` | `Short` | `177.50` | 4,480,000.00 USD | 2,880.00 USD | 0.00 USD | `+41.12%` | `16.20` |
| `Live` | `Short` | `181.50` | 4,480,000.00 USD | 2,170.00 USD | 0.00 USD | `+44.30%` | `11.93` |
| `Live` | `Short` | `183.50` | 4,520,000.00 USD | 32,930.00 USD | 0.00 USD | `+45.89%` | `179.47` |
| `Live` | `Short` | `184.50` | 4,630,000.00 USD | 110,700.00 USD | 0.00 USD | `+46.68%` | `600.00` |
| `Live` | `Short` | `186.50` | 4,950,000.00 USD | 325,990.00 USD | 0.00 USD | `+48.27%` | `1,747.94` |
| `Live` | `Short` | `187.50` | 4,960,000.00 USD | 4,230.00 USD | 0.00 USD | `+49.07%` | `22.56` |
| `Live` | `Short` | `189.50` | 4,960,000.00 USD | 295.62 USD | 0.00 USD | `+50.66%` | `1.56` |
| `Live` | `Short` | `193.50` | 4,980,000.00 USD | 16,500.00 USD | 0.00 USD | `+53.84%` | `85.28` |
| `Live` | `Short` | `195.50` | 4,980,000.00 USD | 2,150.00 USD | 0.00 USD | `+55.43%` | `11.01` |
| `Live` | `Short` | `196.50` | 8,320,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+56.23%` | `17,000.00` |
| `Live` | `Short` | `197.50` | 8,320,000.00 USD | 5,330.00 USD | 0.00 USD | `+57.02%` | `27.00` |
| `Live` | `Short` | `200.50` | 8,330,000.00 USD | 9,850.00 USD | 0.00 USD | `+59.41%` | `49.15` |
| `Live` | `Short` | `201.50` | 8,370,000.00 USD | 38,690.00 USD | 0.00 USD | `+60.20%` | `192.00` |
| `Live` | `Short` | `203.50` | 8,370,000.00 USD | 372.41 USD | 0.00 USD | `+61.79%` | `1.83` |
| `Live` | `Short` | `205.50` | 8,460,000.00 USD | 84,610.00 USD | 0.00 USD | `+63.38%` | `411.72` |
| `Live` | `Short` | `209.50` | 8,480,000.00 USD | 21,090.00 USD | 0.00 USD | `+66.56%` | `100.65` |
| `Live` | `Short` | `210.50` | 8,490,000.00 USD | 9,870.00 USD | 0.00 USD | `+67.36%` | `46.87` |
| `Live` | `Short` | `217.50` | 11,870,000.00 USD | 3,380,000.00 USD | 0.00 USD | `+72.92%` | `15,561.48` |
| `Live` | `Short` | `220.50` | 11,870,000.00 USD | 2,000.00 USD | 0.00 USD | `+75.31%` | `9.06` |
| `Live` | `Short` | `221.50` | 12,940,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+76.10%` | `4,808.67` |
| `Live` | `Short` | `225.50` | 12,940,000.00 USD | 904.25 USD | 0.00 USD | `+79.28%` | `4.01` |
| `Live` | `Short` | `230.50` | 12,940,000.00 USD | 2,310.00 USD | 0.00 USD | `+83.26%` | `10.00` |
| `Live` | `Short` | `232.50` | 13,760,000.00 USD | 818,270.00 USD | 0.00 USD | `+84.85%` | `3,519.45` |
| `Live` | `Short` | `234.50` | 13,760,000.00 USD | 255.61 USD | 0.00 USD | `+86.44%` | `1.09` |
| `Live` | `Short` | `236.50` | 13,760,000.00 USD | 946.00 USD | 0.00 USD | `+88.03%` | `4.00` |
| `Live` | `Short` | `238.50` | 13,920,000.00 USD | 159,310.00 USD | 0.00 USD | `+89.62%` | `667.95` |
| `Live` | `Short` | `240.50` | 13,920,000.00 USD | 2,510.00 USD | 0.00 USD | `+91.21%` | `10.44` |
| `Live` | `Short` | `242.50` | 13,920,000.00 USD | 409.82 USD | 0.00 USD | `+92.80%` | `1.69` |
| `Live` | `Short` | `243.50` | 13,940,000.00 USD | 14,610.00 USD | 0.00 USD | `+93.59%` | `60.00` |
| `Live` | `Short` | `245.50` | 14,010,000.00 USD | 66,220.00 USD | 0.00 USD | `+95.18%` | `269.73` |
| `Live` | `Short` | `248.50` | 14,060,000.00 USD | 50,900.00 USD | 0.00 USD | `+97.57%` | `204.83` |

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
  * Current Rate: `752.92` | Last 24h: `2.78K` | Last 3d: `40.34K` | Last 7d: `111.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0011%` | **USDT OKX** | `0.0002%` |
| **USDT Bybit** | `0.0005%` | **USDT KuCoin** | `0.0002%` |
| **USDT MEXC** | `0.0010%` | **USDT BingX** | `0.0011%` |
| **USDT Gate** | `-0.0027%` | **USDT Bitget** | `0.0009%` |
| **CoinM Binance** | `0.1862%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `125.27` | `125.16` | `125.27` | `125.47` | `124.73` | 786,073.81 USD | 420,964.65 USD | 365,109.16 USD | 55,855.49 USD | `+7.11%` | `10B / 9S` |
| `5:00 UTC` | `125.00` | `125.10` | `125.00` | `125.53` | `124.66` | 887,277.31 USD | 387,796.46 USD | 499,480.85 USD | -111,684.39 USD | `-12.59%` | `10B / 23S` |
| `0:00 UTC` | `124.45` | `124.82` | `124.45` | `125.66` | `124.31` | 1,781,424.08 USD | 591,700.01 USD | 1,189,724.07 USD | -598,024.06 USD | `-33.57%` | `13B / 39S` |
| `5:00 UTC` | `124.41` | `124.42` | `124.41` | `124.69` | `124.20` | 1,280,426.88 USD | 695,542.34 USD | 584,884.54 USD | 110,657.80 USD | `+8.64%` | `8B / 5S` |
| `0:00 UTC` | `124.56` | `124.51` | `124.56` | `124.78` | `124.10` | 675,363.07 USD | 319,234.27 USD | 356,128.80 USD | -36,894.54 USD | `-5.46%` | `7B / 14S` |
| `5:00 UTC` | `124.98` | `124.71` | `124.98` | `125.06` | `124.30` | 643,674.29 USD | 263,568.94 USD | 380,105.36 USD | -116,536.42 USD | `-18.10%` | `5B / 12S` |
| `0:00 UTC` | `124.53` | `124.54` | `124.53` | `125.02` | `124.28` | 704,011.73 USD | 281,288.21 USD | 422,723.52 USD | -141,435.31 USD | `-20.09%` | `3B / 19S` |
| `5:00 UTC` | `124.22` | `124.45` | `124.22` | `124.93` | `124.16` | 840,093.93 USD | 393,249.05 USD | 446,844.88 USD | -53,595.83 USD | `-6.38%` | `11B / 19S` |
| `0:00 UTC` | `124.91` | `124.78` | `124.91` | `125.12` | `124.25` | 1,493,433.04 USD | 622,312.38 USD | 871,120.65 USD | -248,808.27 USD | `-16.66%` | `11B / 18S` |
| `5:00 UTC` | `125.12` | `125.08` | `125.12` | `125.90` | `124.31` | 1,387,702.25 USD | 804,203.56 USD | 583,498.69 USD | 220,704.88 USD | `+15.90%` | `47B / 16S` |

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
| `5m` | 0.00 USD | 242,120.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | 614,450.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 324,690.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 164,730.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | -187,230.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | 217,950.00 USD | **`ACCUMULATION`** |
| `6h` | 0.00 USD | 3,450,000.00 USD | **`ACCUMULATION`** |
| `8h` | 0.00 USD | 6,240,000.00 USD | **`ACCUMULATION`** |
| `12h` | 0.00 USD | 5,340,000.00 USD | **`ACCUMULATION`** |
| `24h` | 0.00 USD | -8,350,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -44,040,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -94,050,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+242.12K` | 15m=`+614.45K` | 1h=`+164.73K` | 24h=`-8.35M`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `119.87` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `118.22` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `123.99`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `127.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `128.72` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `122.94`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`127.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
