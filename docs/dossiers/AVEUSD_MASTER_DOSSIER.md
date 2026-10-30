# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:22:12 IST` (`2026-10-30 03:52:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `124.01` | **Live Ask Quote**: `124.33` | **Mid Price**: `124.17`
- **Spread Points**: `32.00` | **Spread BPS**: `25.77 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `119.24` | VWAP Z-Score: `+2.55` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `1.67` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `55.26` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `124.30` | Lower -3.00σ Band: `114.19`
  * Upper +2.51σ Band: `123.47` | Lower -2.51σ Band: `115.02`
  * Upper +2.01σ Band: `122.63` | Lower -2.01σ Band: `115.86`
  * Upper +2.00σ Band: `122.61` | Lower -2.00σ Band: `115.88`
  * Upper +1.28σ Band: `121.40` | Lower -1.28σ Band: `117.09`
  * Upper +1.00σ Band: `120.93` | Lower -1.00σ Band: `117.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`121.43` | EMA-20=`121.54` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`124.73` (Slope: `+0.0000`) | EMA-100=`127.62`
  * Institutional Anchors: EMA-144=`128.82` | EMA-200=`129.72` (Slope: `-0.8939`) | EMA-233=`130.23`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `123.30` (Distance: `+0.69%`)
  * Point of Control (POC) = `119.02` (Distance: `+4.32%`)
  * Value Area Low (VAL) = `117.73` (Distance: `+5.46%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.01` | Weekly POC=`135.06` | Weekly VAL=`130.78`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`124.67` | Low=`123.67`
  * New York Session (13:00-21:00 UTC): High=`124.92` | Low=`123.42`
  * Initial Balance (First Hour): IB High=`124.54` | IB Low=`123.80`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `123.67` - `124.67`
  * Optimal Trade Entry (OTE 0.705): `124.42`
  * Structural Invalidation Anchor (0.786): `125.16`

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
| --- | **`124.17`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `411` | `0x3ee5...4fab` | `LONG` | 5,351,487.31 USD | `43,303.83` | `77.35` | `123.73` | `75.36` | 2,001,797.27 USD | `+37.41%` | `10X Cross` |
| `737` | `0xecb6...2b00` | `SHORT` | 3,077,828.33 USD | `24,873.35` | `133.17` | `123.73` | `1206.27` | 234,620.08 USD | `+7.62%` | `10X Cross` |
| `799` | `0x0514...bdfe` | `SHORT` | 2,844,180.00 USD | `23,000.00` | `87.41` | `123.73` | `154.88` | -833,700.78 USD | `-29.31%` | `10X Cross` |
| `846` | `0x08c1...1135` | `LONG` | 2,698,515.12 USD | `21,836.18` | `80.89` | `123.73` | `86.72` | 932,180.77 USD | `+34.54%` | `10X Cross` |
| `1030` | `0x0996...0ba6` | `SHORT` | 2,103,260.40 USD | `17,000.00` | `107.97` | `123.73` | `196.58` | -267,687.10 USD | `-12.73%` | `3X Cross` |
| `1134` | `0x45d2...4029` | `SHORT` | 1,944,844.91 USD | `15,721.00` | `118.40` | `123.73` | `2736.15` | -83,453.73 USD | `-4.29%` | `10X Cross` |
| `1148` | `0xbfc7...80b4` | `SHORT` | 1,923,398.93 USD | `15,561.48` | `115.30` | `123.73` | `232.70` | -129,099.60 USD | `-6.71%` | `10X Cross` |
| `1166` | `0x6540...f7b7` | `LONG` | 1,900,735.31 USD | `15,361.96` | `144.40` | `123.73` | `76.39` | -317,470.65 USD | `-16.70%` | `5X Isolated` |
| `1223` | `0x07fd...689d` | `LONG` | 1,799,156.48 USD | `14,552.75` | `148.42` | `123.73` | `0.000000` | -360,781.44 USD | `-20.05%` | `10X Cross` |
| `1453` | `0xcac1...26b3` | `SHORT` | 1,484,640.00 USD | `12,000.00` | `125.37` | `123.73` | `842.99` | 19,800.86 USD | `+1.33%` | `10X Cross` |
| `1455` | `0x12d2...f97f` | `LONG` | 1,479,865.65 USD | `11,961.41` | `133.88` | `123.73` | `0.000000` | -121,538.79 USD | `-8.21%` | `10X Cross` |
| `1473` | `0xeadc...9d55` | `LONG` | 1,462,973.62 USD | `11,823.92` | `89.93` | `123.73` | `0.000000` | 399,617.21 USD | `+27.32%` | `10X Cross` |
| `1644` | `0x9df2...c665` | `SHORT` | 1,284,442.24 USD | `10,380.17` | `133.78` | `123.73` | `3061.95` | 104,267.04 USD | `+8.12%` | `10X Cross` |
| `1700` | `0x3dc9...54b0` | `SHORT` | 1,235,700.00 USD | `10,000.00` | `128.60` | `123.73` | `1833.58` | 50,321.83 USD | `+4.07%` | `10X Cross` |
| `1823` | `0x8af7...fa05` | `SHORT` | 1,130,027.55 USD | `9,133.75` | `131.49` | `123.73` | `2199.17` | 70,953.20 USD | `+6.28%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `137.76` | 52.35 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Long: 0.05K USD at 137.7600 USD [API] | `2026-10-28 20:00:18` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`125.06` (Vol: 442,800.00 USD, Dist: `+0.86%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.03%`)
  * 48H Horizon: Short MP=`125.02` (Vol: 442,800.00 USD, Dist: `+0.83%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.03%`)
  * 3D Horizon: Short MP=`125.02` (Vol: 442,800.00 USD, Dist: `+0.83%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.03%`)
  * 7D Horizon: Short MP=`125.05` (Vol: 442,800.00 USD, Dist: `+0.85%`) | Long MP=`116.46` (Vol: 253,400.00 USD, Dist: `--6.07%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `25.50` | 17,820.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 2,770.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 5,130.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 7,840.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 193.20 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 1,170.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 560.27 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 1,890.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 1,020.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 1,950.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 6,870.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 551.58 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 985.67 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 28,940.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 427.77 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 158.40 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 25,060.00 USD | 9,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,740.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 603.17 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 273.68 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 68,850.00 USD | 9,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 3,560.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 70,910.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 101.08 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 30,120.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 10,790.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 24,340.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 991.94 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 4,270.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 580.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 24,210.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,180,000.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 12,440.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 305.90 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 8,640.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 4,130.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 139.42 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 1,910,000.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 2,880.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 21,750.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 42,100.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 9,730.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,710.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 15,670.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 78,160.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 2,600.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 7,770.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 95,600.00 USD | 5,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 38,430.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 4,310,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 79,800.00 USD | 900,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 32,170.00 USD | 820,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 24,450.00 USD | 788,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 35,220.00 USD | 763,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 11,110.00 USD | 728,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 32,840.00 USD | 717,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 7,830.00 USD | 684,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 34,840.00 USD | 676,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 5,490.00 USD | 642,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,580.00 USD | 636,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 516,660.00 USD | 633,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 17,210.00 USD | 117,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 100,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 52,470.00 USD | 66,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 10,290.00 USD | 13,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,960.00 USD | 3,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 470.44 USD | 470.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 1,190.00 USD | 1,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 1,080.00 USD | 2,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 4,890.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 4,270.00 USD | 11,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 22,550.00 USD | 33,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 17,090.00 USD | 51,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 3,720.00 USD | 54,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 10,710.00 USD | 65,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 10,030.00 USD | 75,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 163,050.00 USD | 238,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 85,740.00 USD | 324,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 1,180.00 USD | 325,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 328,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 328,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 329,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 23,900.00 USD | 353,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,530.00 USD | 356,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 13,630.00 USD | 369,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 567,130.00 USD | 936,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 2,490.00 USD | 939,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 4,930.00 USD | 944,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 167.06 USD | 944,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 12,580.00 USD | 956,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 3,580,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 1,600.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 49,650.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 169.78 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 1,610.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 1,110.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 356,810.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 1,890.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,540.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 295.62 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 34,040.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 815.67 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 26,950.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 480.26 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `207.50` | 5,600.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `212.50` | 15,300.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `213.50` | 25,620.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `217.50` | 726.45 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `221.50` | 9,080.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `224.50` | 5,810.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `231.50` | 2,310.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 9,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `233.50` | 70,050.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 192.29 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `235.50` | 256.69 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `236.50` | 1,070,000.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `241.50` | 132.83 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `243.50` | 65,680.00 USD | 10,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 9,300,000.00 USD | 0.00 USD | 17,820.00 USD | `-79.05%` | `698.90` |
| `Live` | `Long` | `28.50` | 9,280,000.00 USD | 0.00 USD | 2,770.00 USD | `-76.59%` | `97.23` |
| `Live` | `Long` | `30.50` | 9,280,000.00 USD | 0.00 USD | 5,130.00 USD | `-74.94%` | `168.23` |
| `Live` | `Long` | `31.50` | 9,270,000.00 USD | 0.00 USD | 7,840.00 USD | `-74.12%` | `248.76` |
| `Live` | `Long` | `34.50` | 9,270,000.00 USD | 0.00 USD | 193.20 USD | `-71.66%` | `5.60` |
| `Live` | `Long` | `35.50` | 9,270,000.00 USD | 0.00 USD | 1,170.00 USD | `-70.84%` | `32.96` |
| `Live` | `Long` | `36.50` | 9,260,000.00 USD | 0.00 USD | 560.27 USD | `-70.02%` | `15.35` |
| `Live` | `Long` | `37.50` | 9,260,000.00 USD | 0.00 USD | 1,890.00 USD | `-69.19%` | `50.41` |
| `Live` | `Long` | `38.50` | 9,260,000.00 USD | 0.00 USD | 1,020.00 USD | `-68.37%` | `26.41` |
| `Live` | `Long` | `40.50` | 9,260,000.00 USD | 0.00 USD | 1,950.00 USD | `-66.73%` | `48.24` |
| `Live` | `Long` | `41.50` | 9,260,000.00 USD | 0.00 USD | 6,870.00 USD | `-65.91%` | `165.49` |
| `Live` | `Long` | `43.50` | 9,250,000.00 USD | 0.00 USD | 551.58 USD | `-64.27%` | `12.68` |
| `Live` | `Long` | `44.50` | 9,250,000.00 USD | 0.00 USD | 985.67 USD | `-63.44%` | `22.15` |
| `Live` | `Long` | `45.50` | 9,250,000.00 USD | 0.00 USD | 28,940.00 USD | `-62.62%` | `636.08` |
| `Live` | `Long` | `48.50` | 9,220,000.00 USD | 0.00 USD | 427.77 USD | `-60.16%` | `8.82` |
| `Live` | `Long` | `49.50` | 9,220,000.00 USD | 0.00 USD | 158.40 USD | `-59.34%` | `3.20` |
| `Live` | `Long` | `51.50` | 9,220,000.00 USD | 0.00 USD | 25,060.00 USD | `-57.69%` | `486.56` |
| `Live` | `Long` | `54.50` | 9,200,000.00 USD | 0.00 USD | 805.51 USD | `-55.23%` | `14.78` |
| `Live` | `Long` | `56.50` | 9,190,000.00 USD | 0.00 USD | 1,740.00 USD | `-53.59%` | `30.78` |
| `Live` | `Long` | `57.50` | 9,190,000.00 USD | 0.00 USD | 603.17 USD | `-52.76%` | `10.49` |
| `Live` | `Long` | `58.50` | 9,190,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.94%` | `27.49` |
| `Live` | `Long` | `60.50` | 9,190,000.00 USD | 0.00 USD | 1,690.00 USD | `-50.30%` | `27.87` |
| `Live` | `Long` | `61.50` | 9,190,000.00 USD | 0.00 USD | 273.68 USD | `-49.48%` | `4.45` |
| `Live` | `Long` | `62.50` | 9,190,000.00 USD | 0.00 USD | 68,850.00 USD | `-48.66%` | `1,101.57` |
| `Live` | `Long` | `63.50` | 9,120,000.00 USD | 0.00 USD | 3,560.00 USD | `-47.84%` | `56.00` |
| `Live` | `Long` | `65.50` | 9,120,000.00 USD | 0.00 USD | 70,910.00 USD | `-46.19%` | `1,082.63` |
| `Live` | `Long` | `66.50` | 9,050,000.00 USD | 0.00 USD | 101.08 USD | `-45.37%` | `1.52` |
| `Live` | `Long` | `67.50` | 9,050,000.00 USD | 0.00 USD | 30,120.00 USD | `-44.55%` | `446.20` |
| `Live` | `Long` | `68.50` | 9,020,000.00 USD | 0.00 USD | 10,790.00 USD | `-43.73%` | `157.58` |
| `Live` | `Long` | `69.50` | 9,000,000.00 USD | 0.00 USD | 24,340.00 USD | `-42.91%` | `350.19` |
| `Live` | `Long` | `70.50` | 8,980,000.00 USD | 0.00 USD | 991.94 USD | `-42.08%` | `14.07` |
| `Live` | `Long` | `71.50` | 8,980,000.00 USD | 0.00 USD | 4,270.00 USD | `-41.26%` | `59.70` |
| `Live` | `Long` | `72.50` | 8,980,000.00 USD | 0.00 USD | 580.00 USD | `-40.44%` | `8.00` |
| `Live` | `Long` | `73.50` | 8,970,000.00 USD | 0.00 USD | 24,210.00 USD | `-39.62%` | `329.40` |
| `Live` | `Long` | `74.50` | 8,950,000.00 USD | 0.00 USD | 1,060.00 USD | `-38.80%` | `14.20` |
| `Live` | `Long` | `76.50` | 8,950,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-37.16%` | `15,425.80` |
| `Live` | `Long` | `77.50` | 7,770,000.00 USD | 0.00 USD | 9,050.00 USD | `-36.33%` | `116.79` |
| `Live` | `Long` | `78.50` | 7,760,000.00 USD | 0.00 USD | 12,440.00 USD | `-35.51%` | `158.49` |
| `Live` | `Long` | `79.50` | 7,750,000.00 USD | 0.00 USD | 6,790.00 USD | `-34.69%` | `85.43` |
| `Live` | `Long` | `80.50` | 7,740,000.00 USD | 0.00 USD | 305.90 USD | `-33.87%` | `3.80` |
| `Live` | `Long` | `82.50` | 7,740,000.00 USD | 0.00 USD | 8,640.00 USD | `-32.23%` | `104.75` |
| `Live` | `Long` | `83.50` | 7,730,000.00 USD | 0.00 USD | 4,130.00 USD | `-31.41%` | `49.50` |
| `Live` | `Long` | `84.50` | 7,730,000.00 USD | 0.00 USD | 139.42 USD | `-30.58%` | `1.65` |
| `Live` | `Long` | `85.50` | 7,730,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-29.76%` | `22,360.18` |
| `Live` | `Long` | `86.50` | 5,820,000.00 USD | 0.00 USD | 2,880.00 USD | `-28.94%` | `33.34` |
| `Live` | `Long` | `87.50` | 5,810,000.00 USD | 0.00 USD | 21,750.00 USD | `-28.12%` | `248.62` |
| `Live` | `Long` | `88.50` | 5,790,000.00 USD | 0.00 USD | 2,050.00 USD | `-27.30%` | `23.18` |
| `Live` | `Long` | `89.50` | 5,790,000.00 USD | 0.00 USD | 42,100.00 USD | `-26.48%` | `470.39` |
| `Live` | `Long` | `90.50` | 5,750,000.00 USD | 0.00 USD | 9,730.00 USD | `-25.66%` | `107.47` |
| `Live` | `Long` | `91.50` | 5,740,000.00 USD | 0.00 USD | 277,710.00 USD | `-24.83%` | `3,035.05` |
| `Live` | `Long` | `92.50` | 5,460,000.00 USD | 0.00 USD | 15,670.00 USD | `-24.01%` | `169.39` |
| `Live` | `Long` | `93.50` | 5,440,000.00 USD | 0.00 USD | 10,990.00 USD | `-23.19%` | `117.52` |
| `Live` | `Long` | `94.50` | 5,430,000.00 USD | 0.00 USD | 78,160.00 USD | `-22.37%` | `827.11` |
| `Live` | `Long` | `95.50` | 5,350,000.00 USD | 0.00 USD | 2,600.00 USD | `-21.55%` | `27.20` |
| `Live` | `Long` | `96.50` | 5,350,000.00 USD | 0.00 USD | 7,770.00 USD | `-20.73%` | `80.47` |
| `Live` | `Long` | `97.50` | 5,340,000.00 USD | 0.00 USD | 95,600.00 USD | `-19.90%` | `980.51` |
| `Live` | `Long` | `98.50` | 5,250,000.00 USD | 0.00 USD | 38,430.00 USD | `-19.08%` | `390.15` |
| `Live` | `Long` | `99.50` | 5,210,000.00 USD | 0.00 USD | 4,310,000.00 USD | `-18.26%` | `43,317.84` |
| `Live` | `Long` | `100.50` | 900,290.00 USD | 0.00 USD | 79,800.00 USD | `-17.44%` | `794.05` |
| `Live` | `Long` | `101.50` | 820,490.00 USD | 0.00 USD | 32,170.00 USD | `-16.62%` | `316.97` |
| `Live` | `Long` | `102.50` | 788,320.00 USD | 0.00 USD | 24,450.00 USD | `-15.80%` | `238.50` |
| `Live` | `Long` | `103.50` | 763,870.00 USD | 0.00 USD | 35,220.00 USD | `-14.98%` | `340.33` |
| `Live` | `Long` | `104.50` | 728,650.00 USD | 0.00 USD | 11,110.00 USD | `-14.15%` | `106.30` |
| `Live` | `Long` | `105.50` | 717,540.00 USD | 0.00 USD | 32,840.00 USD | `-13.33%` | `311.28` |
| `Live` | `Long` | `106.50` | 684,700.00 USD | 0.00 USD | 7,830.00 USD | `-12.51%` | `73.52` |
| `Live` | `Long` | `107.50` | 676,870.00 USD | 0.00 USD | 34,840.00 USD | `-11.69%` | `324.07` |
| `Live` | `Long` | `108.50` | 642,030.00 USD | 0.00 USD | 5,490.00 USD | `-10.87%` | `50.63` |
| `Live` | `Long` | `109.50` | 636,540.00 USD | 0.00 USD | 2,580.00 USD | `-10.05%` | `23.55` |
| `Live` | `Long` | `110.50` | 633,960.00 USD | 0.00 USD | 516,660.00 USD | `-9.23%` | `4,675.68` |
| `Live` | `Long` | `111.50` | 117,290.00 USD | 0.00 USD | 17,210.00 USD | `-8.40%` | `154.34` |
| `Live` | `Long` | `112.50` | 100,090.00 USD | 0.00 USD | 33,900.00 USD | `-7.58%` | `301.33` |
| `Live` | `Long` | `113.50` | 66,190.00 USD | 0.00 USD | 52,470.00 USD | `-6.76%` | `462.28` |
| `Live` | `Long` | `114.50` | 13,720.00 USD | 0.00 USD | 10,290.00 USD | `-5.94%` | `89.86` |
| `Live` | `Long` | `115.50` | 3,430.00 USD | 0.00 USD | 2,960.00 USD | `-5.12%` | `25.61` |
| `Live` | `Long` | `118.50` | 470.44 USD | 0.00 USD | 470.44 USD | `-2.65%` | `3.97` |
| `Live` | `Short` | `122.50` | 1,190.00 USD | 1,190.00 USD | 0.00 USD | `+0.63%` | `9.70` |
| `Live` | `Short` | `123.50` | 2,270.00 USD | 1,080.00 USD | 0.00 USD | `+1.45%` | `8.73` |
| `Live` | `Short` | `124.50` | 7,150.00 USD | 4,890.00 USD | 0.00 USD | `+2.28%` | `39.24` |
| `Live` | `Short` | `125.50` | 11,430.00 USD | 4,270.00 USD | 0.00 USD | `+3.10%` | `34.05` |
| `Live` | `Short` | `126.50` | 33,970.00 USD | 22,550.00 USD | 0.00 USD | `+3.92%` | `178.24` |
| `Live` | `Short` | `128.50` | 51,060.00 USD | 17,090.00 USD | 0.00 USD | `+5.56%` | `132.99` |
| `Live` | `Short` | `129.50` | 54,780.00 USD | 3,720.00 USD | 0.00 USD | `+6.38%` | `28.74` |
| `Live` | `Short` | `130.50` | 65,490.00 USD | 10,710.00 USD | 0.00 USD | `+7.20%` | `82.08` |
| `Live` | `Short` | `131.50` | 75,520.00 USD | 10,030.00 USD | 0.00 USD | `+8.03%` | `76.26` |
| `Live` | `Short` | `132.50` | 238,570.00 USD | 163,050.00 USD | 0.00 USD | `+8.85%` | `1,230.55` |
| `Live` | `Short` | `136.50` | 324,310.00 USD | 85,740.00 USD | 0.00 USD | `+12.13%` | `628.11` |
| `Live` | `Short` | `137.50` | 325,480.00 USD | 1,180.00 USD | 0.00 USD | `+12.95%` | `8.55` |
| `Live` | `Short` | `138.50` | 328,330.00 USD | 2,850.00 USD | 0.00 USD | `+13.78%` | `20.56` |
| `Live` | `Short` | `139.50` | 328,430.00 USD | 100.44 USD | 0.00 USD | `+14.60%` | `0.72` |
| `Live` | `Short` | `140.50` | 329,580.00 USD | 1,150.00 USD | 0.00 USD | `+15.42%` | `8.19` |
| `Live` | `Short` | `141.50` | 353,490.00 USD | 23,900.00 USD | 0.00 USD | `+16.24%` | `168.93` |
| `Live` | `Short` | `142.50` | 356,010.00 USD | 2,530.00 USD | 0.00 USD | `+17.06%` | `17.73` |
| `Live` | `Short` | `143.50` | 369,640.00 USD | 13,630.00 USD | 0.00 USD | `+17.88%` | `95.00` |
| `Live` | `Short` | `145.50` | 936,780.00 USD | 567,130.00 USD | 0.00 USD | `+19.53%` | `3,897.82` |
| `Live` | `Short` | `146.50` | 939,270.00 USD | 2,490.00 USD | 0.00 USD | `+20.35%` | `16.98` |
| `Live` | `Short` | `148.50` | 944,200.00 USD | 4,930.00 USD | 0.00 USD | `+21.99%` | `33.20` |
| `Live` | `Short` | `150.50` | 944,360.00 USD | 167.06 USD | 0.00 USD | `+23.63%` | `1.11` |
| `Live` | `Short` | `151.50` | 956,940.00 USD | 12,580.00 USD | 0.00 USD | `+24.46%` | `83.02` |
| `Live` | `Short` | `155.50` | 4,540,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+27.74%` | `23,014.13` |
| `Live` | `Short` | `158.50` | 4,540,000.00 USD | 1,480.00 USD | 0.00 USD | `+30.21%` | `9.36` |
| `Live` | `Short` | `160.50` | 4,540,000.00 USD | 1,600.00 USD | 0.00 USD | `+31.85%` | `10.00` |
| `Live` | `Short` | `165.50` | 4,590,000.00 USD | 49,650.00 USD | 0.00 USD | `+35.96%` | `300.00` |
| `Live` | `Short` | `171.50` | 4,590,000.00 USD | 169.78 USD | 0.00 USD | `+40.89%` | `0.99` |
| `Live` | `Short` | `175.50` | 4,590,000.00 USD | 5,620.00 USD | 0.00 USD | `+44.17%` | `32.04` |
| `Live` | `Short` | `178.50` | 4,600,000.00 USD | 1,610.00 USD | 0.00 USD | `+46.64%` | `9.00` |
| `Live` | `Short` | `179.50` | 4,600,000.00 USD | 1,110.00 USD | 0.00 USD | `+47.46%` | `6.20` |
| `Live` | `Short` | `181.50` | 4,950,000.00 USD | 356,810.00 USD | 0.00 USD | `+49.10%` | `1,965.87` |
| `Live` | `Short` | `183.50` | 4,950,000.00 USD | 141.30 USD | 0.00 USD | `+50.74%` | `0.77` |
| `Live` | `Short` | `186.50` | 4,960,000.00 USD | 1,890.00 USD | 0.00 USD | `+53.21%` | `10.15` |
| `Live` | `Short` | `187.50` | 4,960,000.00 USD | 4,540.00 USD | 0.00 USD | `+54.03%` | `24.22` |
| `Live` | `Short` | `189.50` | 4,960,000.00 USD | 295.62 USD | 0.00 USD | `+55.67%` | `1.56` |
| `Live` | `Short` | `190.50` | 4,990,000.00 USD | 34,040.00 USD | 0.00 USD | `+56.49%` | `178.70` |
| `Live` | `Short` | `196.50` | 8,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+61.42%` | `17,013.77` |
| `Live` | `Short` | `197.50` | 8,340,000.00 USD | 815.67 USD | 0.00 USD | `+62.24%` | `4.13` |
| `Live` | `Short` | `200.50` | 8,370,000.00 USD | 26,950.00 USD | 0.00 USD | `+64.71%` | `134.43` |
| `Live` | `Short` | `203.50` | 8,370,000.00 USD | 480.26 USD | 0.00 USD | `+67.17%` | `2.36` |
| `Live` | `Short` | `205.50` | 8,450,000.00 USD | 84,610.00 USD | 0.00 USD | `+68.82%` | `411.72` |
| `Live` | `Short` | `207.50` | 8,460,000.00 USD | 5,600.00 USD | 0.00 USD | `+70.46%` | `27.00` |
| `Live` | `Short` | `210.50` | 8,460,000.00 USD | 151.56 USD | 0.00 USD | `+72.92%` | `0.72` |
| `Live` | `Short` | `212.50` | 8,470,000.00 USD | 15,300.00 USD | 0.00 USD | `+74.57%` | `72.00` |
| `Live` | `Short` | `213.50` | 8,500,000.00 USD | 25,620.00 USD | 0.00 USD | `+75.39%` | `120.00` |
| `Live` | `Short` | `217.50` | 8,500,000.00 USD | 726.45 USD | 0.00 USD | `+78.67%` | `3.34` |
| `Live` | `Short` | `220.50` | 8,500,000.00 USD | 2,000.00 USD | 0.00 USD | `+81.14%` | `9.06` |
| `Live` | `Short` | `221.50` | 8,510,000.00 USD | 9,080.00 USD | 0.00 USD | `+81.96%` | `41.00` |
| `Live` | `Short` | `224.50` | 8,510,000.00 USD | 5,810.00 USD | 0.00 USD | `+84.42%` | `25.90` |
| `Live` | `Short` | `231.50` | 8,520,000.00 USD | 2,310.00 USD | 0.00 USD | `+90.17%` | `10.00` |
| `Live` | `Short` | `232.50` | 9,340,000.00 USD | 818,270.00 USD | 0.00 USD | `+91.00%` | `3,519.45` |
| `Live` | `Short` | `233.50` | 9,410,000.00 USD | 70,050.00 USD | 0.00 USD | `+91.82%` | `300.00` |
| `Live` | `Short` | `234.50` | 9,410,000.00 USD | 192.29 USD | 0.00 USD | `+92.64%` | `0.82` |
| `Live` | `Short` | `235.50` | 9,410,000.00 USD | 256.69 USD | 0.00 USD | `+93.46%` | `1.09` |
| `Live` | `Short` | `236.50` | 10,470,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+94.28%` | `4,508.67` |
| `Live` | `Short` | `240.50` | 10,470,000.00 USD | 103.41 USD | 0.00 USD | `+97.57%` | `0.43` |
| `Live` | `Short` | `241.50` | 10,470,000.00 USD | 132.83 USD | 0.00 USD | `+98.39%` | `0.55` |
| `Live` | `Short` | `243.50` | 10,540,000.00 USD | 65,680.00 USD | 0.00 USD | `+100.03%` | `269.73` |

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
  * Current Rate: `-8.88K` | Last 24h: `15.98K` | Last 3d: `56.03K` | Last 7d: `119.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0088%` | **USDT OKX** | `0.0035%` |
| **USDT Bybit** | `-0.0327%` | **USDT KuCoin** | `0.0000%` |
| **USDT MEXC** | `0.0090%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0013%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-0.0025%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `119.81` | `119.19` | `119.81` | `120.27` | `117.51` | 3,059,962.26 USD | 1,668,626.89 USD | 1,391,335.36 USD | 277,291.53 USD | `+9.06%` | `20B / 9S` |
| `5:00 UTC` | `120.00` | `119.47` | `120.00` | `120.09` | `118.78` | 1,546,202.74 USD | 806,296.59 USD | 739,906.15 USD | 66,390.44 USD | `+4.29%` | `35B / 13S` |
| `0:00 UTC` | `119.72` | `119.95` | `119.72` | `120.84` | `119.12` | 2,078,229.74 USD | 977,317.91 USD | 1,100,911.84 USD | -123,593.93 USD | `-5.95%` | `39B / 19S` |
| `5:00 UTC` | `121.50` | `121.18` | `121.50` | `121.84` | `120.55` | 2,502,423.84 USD | 1,511,661.07 USD | 990,762.77 USD | 520,898.29 USD | `+20.82%` | `32B / 7S` |
| `0:00 UTC` | `121.75` | `121.55` | `121.75` | `121.91` | `120.97` | 1,387,351.12 USD | 687,614.69 USD | 699,736.43 USD | -12,121.73 USD | `-0.87%` | `13B / 15S` |
| `5:00 UTC` | `121.59` | `121.57` | `121.59` | `122.09` | `121.05` | 2,442,757.80 USD | 1,676,951.27 USD | 765,806.53 USD | 911,144.74 USD | `+37.30%` | `26B / 7S` |
| `0:00 UTC` | `122.00` | `121.97` | `122.00` | `122.50` | `121.59` | 2,148,114.65 USD | 949,251.03 USD | 1,198,863.61 USD | -249,612.58 USD | `-11.62%` | `15B / 8S` |
| `5:00 UTC` | `122.60` | `122.32` | `122.60` | `123.18` | `121.75` | 1,556,143.15 USD | 808,945.27 USD | 747,197.89 USD | 61,747.38 USD | `+3.97%` | `36B / 18S` |
| `0:00 UTC` | `123.50` | `123.59` | `123.50` | `124.12` | `122.77` | 1,930,466.83 USD | 1,169,577.61 USD | 760,889.22 USD | 408,688.38 USD | `+21.17%` | `33B / 9S` |
| `5:00 UTC` | `123.97` | `123.97` | `123.97` | `124.13` | `123.78` | 155,347.32 USD | 87,210.57 USD | 68,136.76 USD | 19,073.81 USD | `+12.28%` | `16B / 6S` |

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
| `5m` | 0.00 USD | 258,920.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | 7,350.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 243,520.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 541,100.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | 1,800,000.00 USD | **`ACCUMULATION`** |
| `4h` | 0.00 USD | 180,340.00 USD | **`ACCUMULATION`** |
| `6h` | 0.00 USD | -4,820,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -10,350,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -12,610,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -11,160,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -51,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -99,460,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+258.92K` | 15m=`+7.35K` | 1h=`+541.10K` | 24h=`-11.16M`
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
  * Execution Entry: `117.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `115.25` (Risk Distance: `2.48` pts)
  * +2.5R Take Profit: `123.93`
  * Mathematical Lot Sizing: **`4.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `123.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `125.78` (Risk Distance: `2.48` pts)
  * +2.5R Take Profit: `117.10`
  * Mathematical Lot Sizing: **`4.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`125.16`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
