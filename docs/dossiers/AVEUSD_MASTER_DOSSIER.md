# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:15:37 IST` (`2026-10-30 02:45:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `121.16` | **Live Ask Quote**: `121.48` | **Mid Price**: `121.32`
- **Spread Points**: `32.00` | **Spread BPS**: `26.38 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `121.32` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `122.17` | Lower -3.00σ Band: `120.47`
  * Upper +2.51σ Band: `121.99` | Lower -2.51σ Band: `120.65`
  * Upper +2.01σ Band: `121.83` | Lower -2.01σ Band: `120.81`
  * Upper +2.00σ Band: `121.81` | Lower -2.00σ Band: `120.83`
  * Upper +1.28σ Band: `121.66` | Lower -1.28σ Band: `120.98`
  * Upper +1.00σ Band: `121.56` | Lower -1.00σ Band: `121.08`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`121.32` | EMA-20=`121.32` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`121.32` (Slope: `+0.0000`) | EMA-100=`121.32`
  * Institutional Anchors: EMA-144=`121.32` | EMA-200=`121.32` (Slope: `+0.0000`) | EMA-233=`121.32`
- **Range Boundaries**: 24H High=`122.53` | 24H Low=`120.11` | Weekly High=`123.75` | Weekly Low=`118.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `123.47` (Distance: `-1.73%`)
  * Point of Control (POC) = `119.02` (Distance: `+1.95%`)
  * Value Area Low (VAL) = `117.73` (Distance: `+3.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.01` | Weekly POC=`135.06` | Weekly VAL=`130.78`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`121.81` | Low=`120.83`
  * New York Session (13:00-21:00 UTC): High=`122.05` | Low=`120.59`
  * Initial Balance (First Hour): IB High=`121.68` | IB Low=`120.96`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `120.83` - `121.81`
  * Optimal Trade Entry (OTE 0.705): `121.56`
  * Structural Invalidation Anchor (0.786): `122.29`

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
| --- | **`121.32`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `416` | `0x3ee5...4fab` | `LONG` | 5,261,848.38 USD | `43,303.83` | `77.35` | `121.47` | `99.23` | 1,912,158.34 USD | `+36.34%` | `10X Cross` |
| `750` | `0xecb6...2b00` | `SHORT` | 3,024,054.81 USD | `24,889.34` | `133.17` | `121.47` | `1230.67` | 290,523.03 USD | `+9.61%` | `10X Cross` |
| `811` | `0x0514...bdfe` | `SHORT` | 2,795,190.00 USD | `23,000.00` | `87.41` | `121.47` | `155.11` | -784,710.78 USD | `-28.07%` | `10X Cross` |
| `851` | `0x08c1...1135` | `LONG` | 2,653,314.23 USD | `21,836.18` | `80.89` | `121.47` | `86.10` | 886,979.88 USD | `+33.43%` | `10X Cross` |
| `1050` | `0x0996...0ba6` | `SHORT` | 2,067,200.00 USD | `17,000.00` | `107.97` | `121.47` | `196.58` | -231,626.70 USD | `-11.20%` | `3X Cross` |
| `1142` | `0x45d2...4029` | `SHORT` | 1,911,151.66 USD | `15,721.00` | `118.40` | `121.47` | `2798.66` | -49,760.48 USD | `-2.60%` | `10X Cross` |
| `1160` | `0xbfc7...80b4` | `SHORT` | 1,891,031.05 USD | `15,561.48` | `115.30` | `121.47` | `241.67` | -96,731.73 USD | `-5.12%` | `10X Cross` |
| `1167` | `0x6540...f7b7` | `LONG` | 1,875,220.74 USD | `15,423.76` | `144.40` | `121.47` | `76.39` | -351,908.90 USD | `-18.77%` | `5X Isolated` |
| `1230` | `0x07fd...689d` | `LONG` | 1,781,773.14 USD | `14,662.76` | `148.42` | `121.47` | `0.000000` | -394,492.61 USD | `-22.14%` | `10X Cross` |
| `1475` | `0xcac1...26b3` | `SHORT` | 1,459,200.00 USD | `12,000.00` | `125.37` | `121.47` | `851.72` | 45,240.86 USD | `+3.10%` | `10X Cross` |
| `1478` | `0x12d2...f97f` | `LONG` | 1,453,390.26 USD | `11,961.41` | `133.88` | `121.47` | `0.000000` | -148,014.18 USD | `-10.18%` | `10X Cross` |
| `1494` | `0xeadc...9d55` | `LONG` | 1,436,842.76 USD | `11,823.92` | `89.93` | `121.47` | `0.000000` | 373,486.35 USD | `+25.99%` | `10X Cross` |
| `1653` | `0x9df2...c665` | `SHORT` | 1,261,190.66 USD | `10,380.17` | `133.78` | `121.47` | `3129.86` | 127,518.62 USD | `+10.11%` | `10X Cross` |
| `1707` | `0x3dc9...54b0` | `SHORT` | 1,215,100.00 USD | `10,000.00` | `128.60` | `121.47` | `1875.36` | 70,921.83 USD | `+5.84%` | `10X Cross` |
| `1826` | `0x8af7...fa05` | `SHORT` | 1,110,504.16 USD | `9,133.75` | `131.49` | `121.47` | `2205.82` | 90,476.59 USD | `+8.15%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`126.67` (Vol: 411,400.00 USD, Dist: `+5.00%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`126.73` (Vol: 504,200.00 USD, Dist: `+5.06%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`122.59` (Vol: 457,200.00 USD, Dist: `+1.63%`) | Long MP=`117.89` (Vol: 457,200.00 USD, Dist: `--2.27%`)
  * 7D Horizon: Short MP=`126.74` (Vol: 504,200.00 USD, Dist: `+5.07%`) | Long MP=`117.98` (Vol: 457,200.00 USD, Dist: `--2.19%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `26.50` | 18,520.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 1,440.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 15,680.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 922.62 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 2,320.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 39,280.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 54,350.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 1,070.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 210.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 1,100.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 15,080.00 USD | 9,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 27,310.00 USD | 9,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 1,180.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 2,280.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 158.34 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 2,150.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 158.40 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 4,550.00 USD | 9,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 773.85 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 3,340.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 8,660.00 USD | 9,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 698.75 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 414.51 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 1,740.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 4,830.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 115.94 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 424.27 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,570.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 2,230.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 24,810.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 1,230.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 80,310.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 694.55 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 17,710.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 87,290.00 USD | 9,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,180,000.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 14,120.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 10,320.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 5,980.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 3,500.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 3,390.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 1,850,000.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 44,800.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 2,880.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 22,760.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 15,140.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,910.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,710.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 24,570.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 13,900.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 16,250.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 2,280.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 7,770.00 USD | 5,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 102,330.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 101,270.00 USD | 5,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 14,540.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 4,360,000.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 32,170.00 USD | 893,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 17,370.00 USD | 861,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 35,220.00 USD | 843,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 11,110.00 USD | 808,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 32,820.00 USD | 797,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 10,940.00 USD | 764,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 109,980.00 USD | 753,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 6,350.00 USD | 643,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 6,360.00 USD | 637,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 432,180.00 USD | 631,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 17,970.00 USD | 198,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 38,760.00 USD | 180,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 135,050.00 USD | 142,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 3,990.00 USD | 7,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 3,100.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 19,970.00 USD | 19,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 3,150.00 USD | 23,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 1,010.00 USD | 24,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 2,910.00 USD | 27,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 1,900.00 USD | 28,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 1,750.00 USD | 30,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 120,300.00 USD | 150,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 3,720.00 USD | 154,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 15,800.00 USD | 170,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 807.41 USD | 171,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 185.61 USD | 171,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 85,220.00 USD | 256,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 1,180.00 USD | 257,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 998.59 USD | 258,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 259,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 260,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 517.89 USD | 260,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 9,620.00 USD | 270,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 567,130.00 USD | 837,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 2,720.00 USD | 840,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 13,680.00 USD | 853,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 3,580,000.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 1,600.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 1,910.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 49,650.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 1,550.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 172.75 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 36,150.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 207.67 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 315,500.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 125,340.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 1,130.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 1,890.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 2,330.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 295.62 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 34,760.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 1,250.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `202.50` | 17,270.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `204.50` | 441.72 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 85,010.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `208.50` | 2,830.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `212.50` | 5,740.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `217.50` | 115.28 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 15,730.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `219.50` | 26,340.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `224.50` | 749.83 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 9,590.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `233.50` | 2,590.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 192.29 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 954.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 137,120.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `26.50` | 9,440,000.00 USD | 0.00 USD | 18,520.00 USD | `-77.94%` | `698.90` |
| `Live` | `Long` | `27.50` | 9,420,000.00 USD | 0.00 USD | 1,440.00 USD | `-77.10%` | `52.50` |
| `Live` | `Long` | `28.50` | 9,420,000.00 USD | 0.00 USD | 15,680.00 USD | `-76.27%` | `550.00` |
| `Live` | `Long` | `30.50` | 9,400,000.00 USD | 0.00 USD | 922.62 USD | `-74.61%` | `30.25` |
| `Live` | `Long` | `31.50` | 9,400,000.00 USD | 0.00 USD | 2,320.00 USD | `-73.77%` | `73.67` |
| `Live` | `Long` | `32.50` | 9,400,000.00 USD | 0.00 USD | 39,280.00 USD | `-72.94%` | `1,208.76` |
| `Live` | `Long` | `35.50` | 9,360,000.00 USD | 0.00 USD | 54,350.00 USD | `-70.44%` | `1,531.05` |
| `Live` | `Long` | `36.50` | 9,310,000.00 USD | 0.00 USD | 1,070.00 USD | `-69.61%` | `29.38` |
| `Live` | `Long` | `37.50` | 9,310,000.00 USD | 0.00 USD | 210.00 USD | `-68.78%` | `5.60` |
| `Live` | `Long` | `38.50` | 9,310,000.00 USD | 0.00 USD | 232.54 USD | `-67.95%` | `6.04` |
| `Live` | `Long` | `39.50` | 9,310,000.00 USD | 0.00 USD | 1,100.00 USD | `-67.11%` | `27.97` |
| `Live` | `Long` | `40.50` | 9,300,000.00 USD | 0.00 USD | 15,080.00 USD | `-66.28%` | `372.38` |
| `Live` | `Long` | `42.50` | 9,290,000.00 USD | 0.00 USD | 27,310.00 USD | `-64.62%` | `642.60` |
| `Live` | `Long` | `43.50` | 9,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-63.78%` | `27.07` |
| `Live` | `Long` | `44.50` | 9,260,000.00 USD | 0.00 USD | 2,280.00 USD | `-62.95%` | `51.32` |
| `Live` | `Long` | `45.50` | 9,260,000.00 USD | 0.00 USD | 158.34 USD | `-62.12%` | `3.48` |
| `Live` | `Long` | `47.50` | 9,260,000.00 USD | 0.00 USD | 2,150.00 USD | `-60.45%` | `45.35` |
| `Live` | `Long` | `49.50` | 9,260,000.00 USD | 0.00 USD | 158.40 USD | `-58.79%` | `3.20` |
| `Live` | `Long` | `51.50` | 9,260,000.00 USD | 0.00 USD | 4,550.00 USD | `-57.12%` | `88.41` |
| `Live` | `Long` | `52.50` | 9,250,000.00 USD | 0.00 USD | 773.85 USD | `-56.29%` | `14.74` |
| `Live` | `Long` | `53.50` | 9,250,000.00 USD | 0.00 USD | 3,340.00 USD | `-55.46%` | `62.48` |
| `Live` | `Long` | `54.50` | 9,250,000.00 USD | 0.00 USD | 8,660.00 USD | `-54.62%` | `158.95` |
| `Live` | `Long` | `55.50` | 9,240,000.00 USD | 0.00 USD | 698.75 USD | `-53.79%` | `12.59` |
| `Live` | `Long` | `56.50` | 9,240,000.00 USD | 0.00 USD | 1,510.00 USD | `-52.96%` | `26.66` |
| `Live` | `Long` | `58.50` | 9,240,000.00 USD | 0.00 USD | 1,610.00 USD | `-51.29%` | `27.49` |
| `Live` | `Long` | `60.50` | 9,230,000.00 USD | 0.00 USD | 1,690.00 USD | `-49.63%` | `27.87` |
| `Live` | `Long` | `61.50` | 9,230,000.00 USD | 0.00 USD | 414.51 USD | `-48.80%` | `6.74` |
| `Live` | `Long` | `62.50` | 9,230,000.00 USD | 0.00 USD | 1,740.00 USD | `-47.96%` | `27.92` |
| `Live` | `Long` | `63.50` | 9,230,000.00 USD | 0.00 USD | 4,830.00 USD | `-47.13%` | `76.09` |
| `Live` | `Long` | `65.50` | 9,230,000.00 USD | 0.00 USD | 115.94 USD | `-45.47%` | `1.77` |
| `Live` | `Long` | `66.50` | 9,230,000.00 USD | 0.00 USD | 424.27 USD | `-44.63%` | `6.38` |
| `Live` | `Long` | `67.50` | 9,230,000.00 USD | 0.00 USD | 24,570.00 USD | `-43.80%` | `364.07` |
| `Live` | `Long` | `68.50` | 9,200,000.00 USD | 0.00 USD | 2,230.00 USD | `-42.97%` | `32.58` |
| `Live` | `Long` | `69.50` | 9,200,000.00 USD | 0.00 USD | 24,810.00 USD | `-42.14%` | `356.92` |
| `Live` | `Long` | `70.50` | 9,170,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.30%` | `17.47` |
| `Live` | `Long` | `71.50` | 9,170,000.00 USD | 0.00 USD | 80,310.00 USD | `-40.47%` | `1,123.15` |
| `Live` | `Long` | `72.50` | 9,090,000.00 USD | 0.00 USD | 694.55 USD | `-39.64%` | `9.58` |
| `Live` | `Long` | `73.50` | 9,090,000.00 USD | 0.00 USD | 17,710.00 USD | `-38.81%` | `241.01` |
| `Live` | `Long` | `74.50` | 9,070,000.00 USD | 0.00 USD | 87,290.00 USD | `-37.97%` | `1,171.68` |
| `Live` | `Long` | `76.50` | 8,990,000.00 USD | 0.00 USD | 1,180,000.00 USD | `-36.31%` | `15,441.25` |
| `Live` | `Long` | `77.50` | 7,810,000.00 USD | 0.00 USD | 9,050.00 USD | `-35.48%` | `116.79` |
| `Live` | `Long` | `78.50` | 7,800,000.00 USD | 0.00 USD | 14,120.00 USD | `-34.64%` | `179.87` |
| `Live` | `Long` | `79.50` | 7,780,000.00 USD | 0.00 USD | 10,320.00 USD | `-33.81%` | `129.87` |
| `Live` | `Long` | `80.50` | 7,770,000.00 USD | 0.00 USD | 5,980.00 USD | `-32.98%` | `74.29` |
| `Live` | `Long` | `82.50` | 7,770,000.00 USD | 0.00 USD | 3,500.00 USD | `-31.31%` | `42.37` |
| `Live` | `Long` | `83.50` | 7,760,000.00 USD | 0.00 USD | 3,390.00 USD | `-30.48%` | `40.59` |
| `Live` | `Long` | `84.50` | 7,760,000.00 USD | 0.00 USD | 1,850,000.00 USD | `-29.65%` | `21,939.80` |
| `Live` | `Long` | `85.50` | 5,910,000.00 USD | 0.00 USD | 44,800.00 USD | `-28.82%` | `524.00` |
| `Live` | `Long` | `86.50` | 5,860,000.00 USD | 0.00 USD | 2,880.00 USD | `-27.98%` | `33.34` |
| `Live` | `Long` | `87.50` | 5,860,000.00 USD | 0.00 USD | 22,760.00 USD | `-27.15%` | `260.11` |
| `Live` | `Long` | `88.50` | 5,830,000.00 USD | 0.00 USD | 2,050.00 USD | `-26.32%` | `23.18` |
| `Live` | `Long` | `89.50` | 5,830,000.00 USD | 0.00 USD | 15,140.00 USD | `-25.48%` | `169.16` |
| `Live` | `Long` | `90.50` | 5,820,000.00 USD | 0.00 USD | 6,910.00 USD | `-24.65%` | `76.33` |
| `Live` | `Long` | `91.50` | 5,810,000.00 USD | 0.00 USD | 277,710.00 USD | `-23.82%` | `3,035.05` |
| `Live` | `Long` | `92.50` | 5,530,000.00 USD | 0.00 USD | 24,570.00 USD | `-22.99%` | `265.65` |
| `Live` | `Long` | `93.50` | 5,510,000.00 USD | 0.00 USD | 13,900.00 USD | `-22.15%` | `148.66` |
| `Live` | `Long` | `94.50` | 5,490,000.00 USD | 0.00 USD | 16,250.00 USD | `-21.32%` | `171.97` |
| `Live` | `Long` | `95.50` | 5,480,000.00 USD | 0.00 USD | 2,280.00 USD | `-20.49%` | `23.90` |
| `Live` | `Long` | `96.50` | 5,480,000.00 USD | 0.00 USD | 7,770.00 USD | `-19.66%` | `80.47` |
| `Live` | `Long` | `97.50` | 5,470,000.00 USD | 0.00 USD | 102,330.00 USD | `-18.82%` | `1,049.58` |
| `Live` | `Long` | `98.50` | 5,370,000.00 USD | 0.00 USD | 101,270.00 USD | `-17.99%` | `1,028.09` |
| `Live` | `Long` | `99.50` | 5,260,000.00 USD | 0.00 USD | 14,540.00 USD | `-17.16%` | `146.17` |
| `Live` | `Long` | `100.50` | 5,250,000.00 USD | 0.00 USD | 4,360,000.00 USD | `-16.33%` | `43,350.66` |
| `Live` | `Long` | `101.50` | 893,370.00 USD | 0.00 USD | 32,170.00 USD | `-15.49%` | `316.97` |
| `Live` | `Long` | `102.50` | 861,200.00 USD | 0.00 USD | 17,370.00 USD | `-14.66%` | `169.44` |
| `Live` | `Long` | `103.50` | 843,830.00 USD | 0.00 USD | 35,220.00 USD | `-13.83%` | `340.33` |
| `Live` | `Long` | `104.50` | 808,610.00 USD | 0.00 USD | 11,110.00 USD | `-13.00%` | `106.30` |
| `Live` | `Long` | `105.50` | 797,500.00 USD | 0.00 USD | 32,820.00 USD | `-12.16%` | `311.10` |
| `Live` | `Long` | `106.50` | 764,680.00 USD | 0.00 USD | 10,940.00 USD | `-11.33%` | `102.71` |
| `Live` | `Long` | `107.50` | 753,740.00 USD | 0.00 USD | 109,980.00 USD | `-10.50%` | `1,023.06` |
| `Live` | `Long` | `108.50` | 643,760.00 USD | 0.00 USD | 6,350.00 USD | `-9.67%` | `58.54` |
| `Live` | `Long` | `109.50` | 637,410.00 USD | 0.00 USD | 6,360.00 USD | `-8.83%` | `58.05` |
| `Live` | `Long` | `110.50` | 631,050.00 USD | 0.00 USD | 432,180.00 USD | `-8.00%` | `3,911.13` |
| `Live` | `Long` | `111.50` | 198,870.00 USD | 0.00 USD | 17,970.00 USD | `-7.17%` | `161.20` |
| `Live` | `Long` | `112.50` | 180,900.00 USD | 0.00 USD | 38,760.00 USD | `-6.34%` | `344.49` |
| `Live` | `Long` | `113.50` | 142,140.00 USD | 0.00 USD | 135,050.00 USD | `-5.50%` | `1,189.85` |
| `Live` | `Long` | `114.50` | 7,100.00 USD | 0.00 USD | 3,990.00 USD | `-4.67%` | `34.88` |
| `Live` | `Long` | `115.50` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | `-3.84%` | `26.86` |
| `Live` | `Short` | `121.50` | 19,970.00 USD | 19,970.00 USD | 0.00 USD | `+1.16%` | `164.38` |
| `Live` | `Short` | `122.50` | 23,120.00 USD | 3,150.00 USD | 0.00 USD | `+1.99%` | `25.73` |
| `Live` | `Short` | `123.50` | 24,140.00 USD | 1,010.00 USD | 0.00 USD | `+2.82%` | `8.20` |
| `Live` | `Short` | `124.50` | 27,050.00 USD | 2,910.00 USD | 0.00 USD | `+3.65%` | `23.38` |
| `Live` | `Short` | `125.50` | 28,940.00 USD | 1,900.00 USD | 0.00 USD | `+4.49%` | `15.11` |
| `Live` | `Short` | `126.50` | 30,700.00 USD | 1,750.00 USD | 0.00 USD | `+5.32%` | `13.86` |
| `Live` | `Short` | `128.50` | 150,990.00 USD | 120,300.00 USD | 0.00 USD | `+6.99%` | `936.15` |
| `Live` | `Short` | `129.50` | 154,710.00 USD | 3,720.00 USD | 0.00 USD | `+7.82%` | `28.74` |
| `Live` | `Short` | `130.50` | 170,510.00 USD | 15,800.00 USD | 0.00 USD | `+8.65%` | `121.04` |
| `Live` | `Short` | `131.50` | 171,320.00 USD | 807.41 USD | 0.00 USD | `+9.48%` | `6.14` |
| `Live` | `Short` | `134.50` | 171,500.00 USD | 185.61 USD | 0.00 USD | `+11.98%` | `1.38` |
| `Live` | `Short` | `136.50` | 256,730.00 USD | 85,220.00 USD | 0.00 USD | `+13.65%` | `624.35` |
| `Live` | `Short` | `137.50` | 257,900.00 USD | 1,180.00 USD | 0.00 USD | `+14.48%` | `8.55` |
| `Live` | `Short` | `138.50` | 258,900.00 USD | 998.59 USD | 0.00 USD | `+15.31%` | `7.21` |
| `Live` | `Short` | `139.50` | 259,000.00 USD | 100.44 USD | 0.00 USD | `+16.14%` | `0.72` |
| `Live` | `Short` | `140.50` | 260,150.00 USD | 1,150.00 USD | 0.00 USD | `+16.98%` | `8.19` |
| `Live` | `Short` | `141.50` | 260,670.00 USD | 517.89 USD | 0.00 USD | `+17.81%` | `3.66` |
| `Live` | `Short` | `142.50` | 270,290.00 USD | 9,620.00 USD | 0.00 USD | `+18.64%` | `67.53` |
| `Live` | `Short` | `145.50` | 837,430.00 USD | 567,130.00 USD | 0.00 USD | `+21.14%` | `3,897.82` |
| `Live` | `Short` | `150.50` | 840,150.00 USD | 2,720.00 USD | 0.00 USD | `+25.30%` | `18.09` |
| `Live` | `Short` | `151.50` | 853,830.00 USD | 13,680.00 USD | 0.00 USD | `+26.13%` | `90.30` |
| `Live` | `Short` | `155.50` | 4,430,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+29.46%` | `23,014.13` |
| `Live` | `Short` | `158.50` | 4,430,000.00 USD | 1,480.00 USD | 0.00 USD | `+31.96%` | `9.36` |
| `Live` | `Short` | `160.50` | 4,440,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.63%` | `10.00` |
| `Live` | `Short` | `161.50` | 4,440,000.00 USD | 1,910.00 USD | 0.00 USD | `+34.46%` | `11.81` |
| `Live` | `Short` | `165.50` | 4,490,000.00 USD | 49,650.00 USD | 0.00 USD | `+37.79%` | `300.00` |
| `Live` | `Short` | `172.50` | 4,490,000.00 USD | 1,550.00 USD | 0.00 USD | `+43.62%` | `9.00` |
| `Live` | `Short` | `174.50` | 4,490,000.00 USD | 172.75 USD | 0.00 USD | `+45.28%` | `0.99` |
| `Live` | `Short` | `175.50` | 4,490,000.00 USD | 5,620.00 USD | 0.00 USD | `+46.12%` | `32.04` |
| `Live` | `Short` | `176.50` | 4,530,000.00 USD | 36,150.00 USD | 0.00 USD | `+46.95%` | `204.83` |
| `Live` | `Short` | `177.50` | 4,530,000.00 USD | 207.67 USD | 0.00 USD | `+47.78%` | `1.17` |
| `Live` | `Short` | `180.50` | 4,850,000.00 USD | 315,500.00 USD | 0.00 USD | `+50.28%` | `1,747.94` |
| `Live` | `Short` | `181.50` | 4,970,000.00 USD | 125,340.00 USD | 0.00 USD | `+51.11%` | `690.58` |
| `Live` | `Short` | `182.50` | 4,970,000.00 USD | 1,130.00 USD | 0.00 USD | `+51.94%` | `6.20` |
| `Live` | `Short` | `183.50` | 4,970,000.00 USD | 141.30 USD | 0.00 USD | `+52.78%` | `0.77` |
| `Live` | `Short` | `186.50` | 4,970,000.00 USD | 1,890.00 USD | 0.00 USD | `+55.27%` | `10.15` |
| `Live` | `Short` | `187.50` | 4,980,000.00 USD | 2,330.00 USD | 0.00 USD | `+56.11%` | `12.41` |
| `Live` | `Short` | `189.50` | 4,980,000.00 USD | 295.62 USD | 0.00 USD | `+57.77%` | `1.56` |
| `Live` | `Short` | `194.50` | 5,010,000.00 USD | 34,760.00 USD | 0.00 USD | `+61.93%` | `178.70` |
| `Live` | `Short` | `196.50` | 8,350,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+63.60%` | `17,007.57` |
| `Live` | `Short` | `200.50` | 8,360,000.00 USD | 9,850.00 USD | 0.00 USD | `+66.93%` | `49.15` |
| `Live` | `Short` | `201.50` | 8,370,000.00 USD | 1,250.00 USD | 0.00 USD | `+67.76%` | `6.20` |
| `Live` | `Short` | `202.50` | 8,380,000.00 USD | 17,270.00 USD | 0.00 USD | `+68.60%` | `85.28` |
| `Live` | `Short` | `203.50` | 8,380,000.00 USD | 372.41 USD | 0.00 USD | `+69.43%` | `1.83` |
| `Live` | `Short` | `204.50` | 8,380,000.00 USD | 441.72 USD | 0.00 USD | `+70.26%` | `2.16` |
| `Live` | `Short` | `205.50` | 8,470,000.00 USD | 85,010.00 USD | 0.00 USD | `+71.09%` | `413.69` |
| `Live` | `Short` | `208.50` | 8,470,000.00 USD | 2,830.00 USD | 0.00 USD | `+73.59%` | `13.58` |
| `Live` | `Short` | `210.50` | 8,470,000.00 USD | 151.56 USD | 0.00 USD | `+75.26%` | `0.72` |
| `Live` | `Short` | `212.50` | 8,480,000.00 USD | 5,740.00 USD | 0.00 USD | `+76.92%` | `27.00` |
| `Live` | `Short` | `217.50` | 8,480,000.00 USD | 115.28 USD | 0.00 USD | `+81.08%` | `0.53` |
| `Live` | `Short` | `218.50` | 8,490,000.00 USD | 15,730.00 USD | 0.00 USD | `+81.92%` | `72.00` |
| `Live` | `Short` | `219.50` | 8,520,000.00 USD | 26,340.00 USD | 0.00 USD | `+82.75%` | `120.00` |
| `Live` | `Short` | `220.50` | 8,520,000.00 USD | 2,000.00 USD | 0.00 USD | `+83.58%` | `9.06` |
| `Live` | `Short` | `224.50` | 8,520,000.00 USD | 749.83 USD | 0.00 USD | `+86.91%` | `3.34` |
| `Live` | `Short` | `227.50` | 8,530,000.00 USD | 9,590.00 USD | 0.00 USD | `+89.41%` | `42.16` |
| `Live` | `Short` | `232.50` | 9,350,000.00 USD | 818,270.00 USD | 0.00 USD | `+93.57%` | `3,519.45` |
| `Live` | `Short` | `233.50` | 9,350,000.00 USD | 2,590.00 USD | 0.00 USD | `+94.41%` | `11.09` |
| `Live` | `Short` | `234.50` | 9,350,000.00 USD | 192.29 USD | 0.00 USD | `+95.24%` | `0.82` |
| `Live` | `Short` | `238.50` | 9,350,000.00 USD | 954.00 USD | 0.00 USD | `+98.57%` | `4.00` |
| `Live` | `Short` | `240.50` | 9,490,000.00 USD | 137,120.00 USD | 0.00 USD | `+100.23%` | `570.16` |

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
  * Current Rate: `-4.95K` | Last 24h: `15.98K` | Last 3d: `56.03K` | Last 7d: `119.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0058%` |
| **USDT Bybit** | `-0.0251%` | **USDT KuCoin** | `0.0016%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0022%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0055%` | **CoinM OKX** | `-` |

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
| `5:00 UTC` | `117.22` | `116.97` | `117.22` | `120.02` | `115.02` | 9,861,640.78 USD | 3,876,505.89 USD | 5,985,134.89 USD | -2,108,629.00 USD | `-21.38%` | `2B / 29S` |
| `0:00 UTC` | `117.74` | `117.24` | `117.74` | `118.42` | `115.96` | 3,865,835.63 USD | 1,961,740.56 USD | 1,904,095.08 USD | 57,645.48 USD | `+1.49%` | `20B / 16S` |
| `5:00 UTC` | `118.95` | `118.77` | `118.95` | `119.34` | `118.05` | 3,208,757.12 USD | 1,414,154.79 USD | 1,794,602.33 USD | -380,447.54 USD | `-11.86%` | `12B / 34S` |
| `0:00 UTC` | `118.90` | `119.01` | `118.90` | `119.97` | `118.07` | 2,314,365.12 USD | 1,430,488.25 USD | 883,876.88 USD | 546,611.37 USD | `+23.62%` | `42B / 21S` |
| `5:00 UTC` | `118.70` | `118.80` | `118.70` | `119.53` | `118.31` | 2,154,963.00 USD | 1,005,187.45 USD | 1,149,775.55 USD | -144,588.09 USD | `-6.71%` | `17B / 19S` |
| `0:00 UTC` | `119.81` | `119.19` | `119.81` | `120.27` | `117.51` | 3,059,962.26 USD | 1,668,626.89 USD | 1,391,335.36 USD | 277,291.53 USD | `+9.06%` | `20B / 9S` |
| `5:00 UTC` | `120.00` | `119.47` | `120.00` | `120.09` | `118.78` | 1,546,202.74 USD | 806,296.59 USD | 739,906.15 USD | 66,390.44 USD | `+4.29%` | `35B / 13S` |
| `0:00 UTC` | `119.72` | `119.95` | `119.72` | `120.84` | `119.12` | 2,078,229.74 USD | 977,317.91 USD | 1,100,911.84 USD | -123,593.93 USD | `-5.95%` | `39B / 19S` |
| `5:00 UTC` | `121.50` | `121.18` | `121.50` | `121.84` | `120.55` | 2,502,423.84 USD | 1,511,661.07 USD | 990,762.77 USD | 520,898.29 USD | `+20.82%` | `32B / 7S` |
| `0:00 UTC` | `121.44` | `121.50` | `121.44` | `121.91` | `120.97` | 984,095.09 USD | 486,180.57 USD | 497,914.53 USD | -11,733.96 USD | `-1.19%` | `15B / 14S` |

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
| `5m` | 18,550.00 USD | 111,620.00 USD | **`ACCUMULATION`** |
| `15m` | 160,740.00 USD | 238,250.00 USD | **`ACCUMULATION`** |
| `30m` | 242,500.00 USD | 1,080,000.00 USD | **`ACCUMULATION`** |
| `1h` | 78,240.00 USD | 1,460,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,040,000.00 USD | 2,460,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,260,000.00 USD | -3,460,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,070,000.00 USD | -10,560,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,830,000.00 USD | -11,540,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -7,260,000.00 USD | -13,030,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,030,000.00 USD | -10,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -29,240,000.00 USD | -51,200,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -115,910,000.00 USD | -99,920,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+18.55K` | 15m=`+160.74K` | 1h=`+78.24K` | 24h=`-7.03M`
* Futures Capital Netflows: 5m=`+111.62K` | 15m=`+238.25K` | 1h=`+1.46M` | 24h=`-10.52M`
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
  * Execution Entry: `117.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `116.05` (Risk Distance: `1.68` pts)
  * +2.5R Take Profit: `121.93`
  * Mathematical Lot Sizing: **`5.95 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `123.47` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `125.15` (Risk Distance: `1.68` pts)
  * +2.5R Take Profit: `119.27`
  * Mathematical Lot Sizing: **`5.95 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`122.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
