# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:14:11 IST` (`2026-10-30 05:44:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `126.38` | **Live Ask Quote**: `126.66` | **Mid Price**: `126.52`
- **Spread Points**: `28.00` | **Spread BPS**: `22.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `120.37` | VWAP Z-Score: `+2.11` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `1.47` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `63.65` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `128.33` | Lower -3.00σ Band: `112.41`
  * Upper +2.51σ Band: `127.03` | Lower -2.51σ Band: `113.71`
  * Upper +2.01σ Band: `125.70` | Lower -2.01σ Band: `115.03`
  * Upper +2.00σ Band: `125.68` | Lower -2.00σ Band: `115.06`
  * Upper +1.28σ Band: `123.76` | Lower -1.28σ Band: `116.97`
  * Upper +1.00σ Band: `123.02` | Lower -1.00σ Band: `117.71`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`124.16` | EMA-20=`123.10` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`124.67` (Slope: `+0.0000`) | EMA-100=`127.20`
  * Institutional Anchors: EMA-144=`128.41` | EMA-200=`129.38` (Slope: `-0.5803`) | EMA-233=`129.85`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `123.81` (Distance: `+2.14%`)
  * Point of Control (POC) = `119.02` (Distance: `+6.26%`)
  * Value Area Low (VAL) = `117.73` (Distance: `+7.42%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.01` | Weekly POC=`135.06` | Weekly VAL=`130.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`126.87` | Low=`123.92`
  * New York Session (13:00-21:00 UTC): High=`127.28` | Low=`125.76`
  * Initial Balance (First Hour): IB High=`126.87` | IB Low=`123.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `126.01` - `127.03`
  * Optimal Trade Entry (OTE 0.705): `126.77`
  * Structural Invalidation Anchor (0.786): `127.53`

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
| --- | **`126.52`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `410` | `0x3ee5...4fab` | `LONG` | 5,480,532.72 USD | `43,303.83` | `77.35` | `126.56` | `72.90` | 2,130,842.68 USD | `+38.88%` | `10X Cross` |
| `730` | `0xecb6...2b00` | `SHORT` | 3,138,372.67 USD | `24,819.08` | `133.17` | `126.56` | `1293.10` | 166,848.46 USD | `+5.32%` | `10X Cross` |
| `787` | `0x0514...bdfe` | `SHORT` | 2,908,120.00 USD | `23,000.00` | `87.41` | `126.56` | `154.33` | -897,640.78 USD | `-30.87%` | `10X Cross` |
| `826` | `0x08c1...1135` | `LONG` | 2,760,748.24 USD | `21,836.18` | `80.89` | `126.56` | `87.49` | 994,413.89 USD | `+36.02%` | `10X Cross` |
| `1020` | `0x0996...0ba6` | `SHORT` | 2,149,862.50 USD | `17,000.00` | `107.97` | `126.56` | `196.58` | -314,289.20 USD | `-14.62%` | `3X Cross` |
| `1112` | `0x45d2...4029` | `SHORT` | 1,988,392.08 USD | `15,721.00` | `118.40` | `126.56` | `2625.77` | -127,000.90 USD | `-6.39%` | `10X Cross` |
| `1128` | `0xbfc7...80b4` | `SHORT` | 1,967,943.66 USD | `15,561.48` | `115.30` | `126.56` | `218.82` | -173,644.34 USD | `-8.82%` | `10X Cross` |
| `1153` | `0x6540...f7b7` | `LONG` | 1,929,454.43 USD | `15,253.81` | `144.40` | `126.56` | `76.39` | -273,135.11 USD | `-14.16%` | `5X Isolated` |
| `1218` | `0x07fd...689d` | `LONG` | 1,812,660.36 USD | `14,332.73` | `148.42` | `126.56` | `0.000000` | -314,621.91 USD | `-17.36%` | `10X Cross` |
| `1440` | `0xcac1...26b3` | `SHORT` | 1,517,550.00 USD | `12,000.00` | `125.37` | `126.56` | `825.66` | -13,109.14 USD | `-0.86%` | `10X Cross` |
| `1445` | `0x12d2...f97f` | `LONG` | 1,512,759.52 USD | `11,961.41` | `133.88` | `126.56` | `0.000000` | -88,644.92 USD | `-5.86%` | `10X Cross` |
| `1459` | `0xeadc...9d55` | `LONG` | 1,495,134.68 USD | `11,823.92` | `89.93` | `126.53` | `0.000000` | 431,778.27 USD | `+28.88%` | `10X Cross` |
| `1612` | `0x9df2...c665` | `SHORT` | 1,312,780.10 USD | `10,380.17` | `133.78` | `126.53` | `2985.11` | 75,929.17 USD | `+5.78%` | `10X Cross` |
| `1668` | `0x3dc9...54b0` | `SHORT` | 1,264,800.00 USD | `10,000.00` | `128.60` | `126.53` | `1739.08` | 21,221.83 USD | `+1.68%` | `10X Cross` |
| `1795` | `0x8af7...fa05` | `SHORT` | 1,155,236.70 USD | `9,133.75` | `131.49` | `126.53` | `2193.26` | 45,744.05 USD | `+3.96%` | `10X Cross` |
| `1987` | `0xbc5b...7fdc` | `LONG` | 1,016,183.98 USD | `8,033.71` | `136.30` | `126.53` | `18.25` | -78,845.23 USD | `-7.76%` | `10X Cross` |
| `1999` | `0x72db...8bb6` | `LONG` | 1,011,600.00 USD | `8,000.00` | `180.99` | `126.53` | `0.000000` | -436,357.43 USD | `-43.14%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `128.46` | 1,821.56 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 1.82K USD at 128.4600 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `128.78` | 291.04 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 0.29K USD at 128.7800 USD [API] | `2026-10-29 02:35:57` |
| `ANNOUNCEMENT` | `INFO` | `128.94` | 281.09 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 0.28K USD at 128.9400 USD [API] | `2026-10-29 02:34:56` |
| `ANNOUNCEMENT` | `INFO` | `128.51` | 803.19 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 0.80K USD at 128.5100 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `128.48` | 391.86 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 0.39K USD at 128.4800 USD [API] | `2026-10-29 02:36:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`128.80` (Vol: 368,100.00 USD, Dist: `+1.87%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--7.85%`)
  * 48H Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+1.88%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--7.85%`)
  * 3D Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+1.88%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--7.85%`)
  * 7D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`116.46` (Vol: 253,400.00 USD, Dist: `--7.89%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `25.50` | 585.23 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 263.94 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 6,990.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 18,190.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 305.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 464.31 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 130,370.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 702.76 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 900.28 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 4,430.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 323.90 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 37,920.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 356.89 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 209.30 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 106.48 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 6,100.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 158.40 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 24,570.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 212.18 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 56,620.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 818.62 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,720.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 4,270.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 1,340.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 3,560.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 313.47 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 115.94 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 6,990.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 33,390.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,110.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 23,780.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 1,970.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,410.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 3,150,000.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,400.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,170,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 13,380.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 3,500.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 11,250.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 15,110.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 44,800.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 4,180.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,990,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 15,140.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,910.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,710.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,750.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 21,890.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 2,600.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 16,010.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 101,140.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 38,430.00 USD | 917,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 1,390.00 USD | 879,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 70,650.00 USD | 877,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 30,490.00 USD | 807,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 91,530.00 USD | 776,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 39,580.00 USD | 685,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 12,210.00 USD | 645,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 24,530.00 USD | 633,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 7,270.00 USD | 608,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 35,300.00 USD | 601,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 8,750.00 USD | 566,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,580.00 USD | 557,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 433,620.00 USD | 554,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 18,290.00 USD | 121,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 102,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 52,030.00 USD | 69,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 16,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,960.00 USD | 12,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 8,270.00 USD | 9,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 1,190.00 USD | 1,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 2,610.00 USD | 2,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 1,940.00 USD | 4,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 33,080.00 USD | 37,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 170,680.00 USD | 208,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 269.57 USD | 208,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 12,430.00 USD | 221,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 15,370.00 USD | 236,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 81,620.00 USD | 318,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 2,850.00 USD | 320,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 323,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 323,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 324,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 23,900.00 USD | 348,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,530.00 USD | 351,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 13,630.00 USD | 365,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 564,450.00 USD | 929,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 732.50 USD | 930,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 167.06 USD | 930,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 12,580.00 USD | 942,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 3,550,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 2,200.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 160.88 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 51,920.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 12,770.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 4,360.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 1,060.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 1,550.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 202.99 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 387.72 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 315,860.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 34,110.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 1,890.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 2,330.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 295.62 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 16,590.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 40,040.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 5,390.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `202.50` | 676.35 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 39,440.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `212.50` | 8,710.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 1,130.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 3,550,000.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 1,020,000.00 USD | 13,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 2,310.00 USD | 13,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `236.50` | 257.79 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 387.99 USD | 13,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 64,970.00 USD | 13,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 8,200,000.00 USD | 0.00 USD | 585.23 USD | `-79.54%` | `22.95` |
| `Live` | `Long` | `26.50` | 8,200,000.00 USD | 0.00 USD | 263.94 USD | `-78.73%` | `9.96` |
| `Live` | `Long` | `27.50` | 8,200,000.00 USD | 0.00 USD | 6,990.00 USD | `-77.93%` | `254.11` |
| `Live` | `Long` | `28.50` | 8,190,000.00 USD | 0.00 USD | 18,190.00 USD | `-77.13%` | `638.20` |
| `Live` | `Long` | `30.50` | 8,170,000.00 USD | 0.00 USD | 305.00 USD | `-75.52%` | `10.00` |
| `Live` | `Long` | `31.50` | 8,170,000.00 USD | 0.00 USD | 464.31 USD | `-74.72%` | `14.74` |
| `Live` | `Long` | `32.50` | 8,170,000.00 USD | 0.00 USD | 130,370.00 USD | `-73.92%` | `4,011.32` |
| `Live` | `Long` | `34.50` | 8,040,000.00 USD | 0.00 USD | 702.76 USD | `-72.31%` | `20.37` |
| `Live` | `Long` | `35.50` | 8,040,000.00 USD | 0.00 USD | 900.28 USD | `-71.51%` | `25.36` |
| `Live` | `Long` | `38.50` | 8,040,000.00 USD | 0.00 USD | 4,430.00 USD | `-69.10%` | `115.00` |
| `Live` | `Long` | `39.50` | 8,030,000.00 USD | 0.00 USD | 323.90 USD | `-68.30%` | `8.20` |
| `Live` | `Long` | `40.50` | 8,030,000.00 USD | 0.00 USD | 37,920.00 USD | `-67.50%` | `936.21` |
| `Live` | `Long` | `44.50` | 7,990,000.00 USD | 0.00 USD | 356.89 USD | `-64.29%` | `8.02` |
| `Live` | `Long` | `45.50` | 7,990,000.00 USD | 0.00 USD | 209.30 USD | `-63.49%` | `4.60` |
| `Live` | `Long` | `46.50` | 7,990,000.00 USD | 0.00 USD | 106.48 USD | `-62.68%` | `2.29` |
| `Live` | `Long` | `47.50` | 7,990,000.00 USD | 0.00 USD | 6,100.00 USD | `-61.88%` | `128.40` |
| `Live` | `Long` | `49.50` | 7,990,000.00 USD | 0.00 USD | 158.40 USD | `-60.28%` | `3.20` |
| `Live` | `Long` | `50.50` | 7,990,000.00 USD | 0.00 USD | 24,570.00 USD | `-59.47%` | `486.56` |
| `Live` | `Long` | `51.50` | 7,960,000.00 USD | 0.00 USD | 212.18 USD | `-58.67%` | `4.12` |
| `Live` | `Long` | `52.50` | 7,960,000.00 USD | 0.00 USD | 56,620.00 USD | `-57.87%` | `1,078.45` |
| `Live` | `Long` | `54.50` | 7,910,000.00 USD | 0.00 USD | 805.51 USD | `-56.26%` | `14.78` |
| `Live` | `Long` | `55.50` | 7,910,000.00 USD | 0.00 USD | 818.62 USD | `-55.46%` | `14.75` |
| `Live` | `Long` | `56.50` | 7,900,000.00 USD | 0.00 USD | 1,720.00 USD | `-54.66%` | `30.46` |
| `Live` | `Long` | `57.50` | 7,900,000.00 USD | 0.00 USD | 4,270.00 USD | `-53.86%` | `74.29` |
| `Live` | `Long` | `58.50` | 7,900,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.05%` | `27.49` |
| `Live` | `Long` | `60.50` | 7,900,000.00 USD | 0.00 USD | 1,690.00 USD | `-51.45%` | `27.87` |
| `Live` | `Long` | `61.50` | 7,900,000.00 USD | 0.00 USD | 168.51 USD | `-50.65%` | `2.74` |
| `Live` | `Long` | `62.50` | 7,900,000.00 USD | 0.00 USD | 1,340.00 USD | `-49.84%` | `21.40` |
| `Live` | `Long` | `63.50` | 7,890,000.00 USD | 0.00 USD | 3,560.00 USD | `-49.04%` | `56.00` |
| `Live` | `Long` | `64.50` | 7,890,000.00 USD | 0.00 USD | 313.47 USD | `-48.24%` | `4.86` |
| `Live` | `Long` | `65.50` | 7,890,000.00 USD | 0.00 USD | 115.94 USD | `-47.44%` | `1.77` |
| `Live` | `Long` | `66.50` | 7,890,000.00 USD | 0.00 USD | 6,990.00 USD | `-46.63%` | `105.14` |
| `Live` | `Long` | `67.50` | 7,880,000.00 USD | 0.00 USD | 33,390.00 USD | `-45.83%` | `494.66` |
| `Live` | `Long` | `68.50` | 7,850,000.00 USD | 0.00 USD | 7,110.00 USD | `-45.03%` | `103.75` |
| `Live` | `Long` | `69.50` | 7,840,000.00 USD | 0.00 USD | 23,780.00 USD | `-44.23%` | `342.17` |
| `Live` | `Long` | `70.50` | 7,820,000.00 USD | 0.00 USD | 1,970.00 USD | `-43.42%` | `27.99` |
| `Live` | `Long` | `71.50` | 7,820,000.00 USD | 0.00 USD | 1,410.00 USD | `-42.62%` | `19.76` |
| `Live` | `Long` | `72.50` | 7,820,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-41.82%` | `43,411.83` |
| `Live` | `Long` | `73.50` | 4,670,000.00 USD | 0.00 USD | 11,400.00 USD | `-41.02%` | `155.11` |
| `Live` | `Long` | `74.50` | 4,660,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.21%` | `14.20` |
| `Live` | `Long` | `76.50` | 4,660,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-38.61%` | `15,344.59` |
| `Live` | `Long` | `77.50` | 3,480,000.00 USD | 0.00 USD | 9,050.00 USD | `-37.81%` | `116.79` |
| `Live` | `Long` | `78.50` | 3,470,000.00 USD | 0.00 USD | 4,310.00 USD | `-37.00%` | `54.87` |
| `Live` | `Long` | `79.50` | 3,470,000.00 USD | 0.00 USD | 13,380.00 USD | `-36.20%` | `168.24` |
| `Live` | `Long` | `82.50` | 3,450,000.00 USD | 0.00 USD | 3,500.00 USD | `-33.79%` | `42.37` |
| `Live` | `Long` | `83.50` | 3,450,000.00 USD | 0.00 USD | 11,250.00 USD | `-32.99%` | `134.77` |
| `Live` | `Long` | `84.50` | 3,440,000.00 USD | 0.00 USD | 15,110.00 USD | `-32.19%` | `178.81` |
| `Live` | `Long` | `85.50` | 3,430,000.00 USD | 0.00 USD | 44,800.00 USD | `-31.39%` | `524.00` |
| `Live` | `Long` | `86.50` | 3,380,000.00 USD | 0.00 USD | 4,180.00 USD | `-30.58%` | `48.34` |
| `Live` | `Long` | `87.50` | 3,380,000.00 USD | 0.00 USD | 1,990,000.00 USD | `-29.78%` | `22,735.52` |
| `Live` | `Long` | `88.50` | 1,390,000.00 USD | 0.00 USD | 2,050.00 USD | `-28.98%` | `23.18` |
| `Live` | `Long` | `89.50` | 1,380,000.00 USD | 0.00 USD | 15,140.00 USD | `-28.18%` | `169.16` |
| `Live` | `Long` | `90.50` | 1,370,000.00 USD | 0.00 USD | 6,910.00 USD | `-27.37%` | `76.33` |
| `Live` | `Long` | `91.50` | 1,360,000.00 USD | 0.00 USD | 277,710.00 USD | `-26.57%` | `3,035.05` |
| `Live` | `Long` | `92.50` | 1,080,000.00 USD | 0.00 USD | 14,750.00 USD | `-25.77%` | `159.47` |
| `Live` | `Long` | `93.50` | 1,070,000.00 USD | 0.00 USD | 10,990.00 USD | `-24.97%` | `117.52` |
| `Live` | `Long` | `94.50` | 1,060,000.00 USD | 0.00 USD | 21,890.00 USD | `-24.16%` | `231.61` |
| `Live` | `Long` | `95.50` | 1,040,000.00 USD | 0.00 USD | 2,600.00 USD | `-23.36%` | `27.20` |
| `Live` | `Long` | `96.50` | 1,030,000.00 USD | 0.00 USD | 16,010.00 USD | `-22.56%` | `165.93` |
| `Live` | `Long` | `97.50` | 1,020,000.00 USD | 0.00 USD | 101,140.00 USD | `-21.76%` | `1,037.30` |
| `Live` | `Long` | `98.50` | 917,530.00 USD | 0.00 USD | 38,430.00 USD | `-20.95%` | `390.15` |
| `Live` | `Long` | `99.50` | 879,100.00 USD | 0.00 USD | 1,390.00 USD | `-20.15%` | `14.01` |
| `Live` | `Long` | `100.50` | 877,710.00 USD | 0.00 USD | 70,650.00 USD | `-19.35%` | `703.00` |
| `Live` | `Long` | `101.50` | 807,060.00 USD | 0.00 USD | 30,490.00 USD | `-18.55%` | `300.36` |
| `Live` | `Long` | `102.50` | 776,570.00 USD | 0.00 USD | 91,530.00 USD | `-17.74%` | `892.97` |
| `Live` | `Long` | `103.50` | 685,040.00 USD | 0.00 USD | 39,580.00 USD | `-16.94%` | `382.39` |
| `Live` | `Long` | `104.50` | 645,460.00 USD | 0.00 USD | 12,210.00 USD | `-16.14%` | `116.83` |
| `Live` | `Long` | `105.50` | 633,260.00 USD | 0.00 USD | 24,530.00 USD | `-15.34%` | `232.55` |
| `Live` | `Long` | `106.50` | 608,720.00 USD | 0.00 USD | 7,270.00 USD | `-14.53%` | `68.28` |
| `Live` | `Long` | `107.50` | 601,450.00 USD | 0.00 USD | 35,300.00 USD | `-13.73%` | `328.39` |
| `Live` | `Long` | `108.50` | 566,150.00 USD | 0.00 USD | 8,750.00 USD | `-12.93%` | `80.63` |
| `Live` | `Long` | `109.50` | 557,400.00 USD | 0.00 USD | 2,580.00 USD | `-12.13%` | `23.55` |
| `Live` | `Long` | `110.50` | 554,820.00 USD | 0.00 USD | 433,620.00 USD | `-11.32%` | `3,924.17` |
| `Live` | `Long` | `111.50` | 121,200.00 USD | 0.00 USD | 18,290.00 USD | `-10.52%` | `164.08` |
| `Live` | `Long` | `112.50` | 102,900.00 USD | 0.00 USD | 33,900.00 USD | `-9.72%` | `301.33` |
| `Live` | `Long` | `113.50` | 69,010.00 USD | 0.00 USD | 52,030.00 USD | `-8.92%` | `458.42` |
| `Live` | `Long` | `114.50` | 16,970.00 USD | 0.00 USD | 4,560.00 USD | `-8.11%` | `39.82` |
| `Live` | `Long` | `115.50` | 12,420.00 USD | 0.00 USD | 2,960.00 USD | `-7.31%` | `25.61` |
| `Live` | `Long` | `116.50` | 9,460.00 USD | 0.00 USD | 8,270.00 USD | `-6.51%` | `71.00` |
| `Live` | `Long` | `117.50` | 1,190.00 USD | 0.00 USD | 1,190.00 USD | `-5.71%` | `10.09` |
| `Live` | `Short` | `125.50` | 2,610.00 USD | 2,610.00 USD | 0.00 USD | `+0.71%` | `20.77` |
| `Live` | `Short` | `126.50` | 4,540.00 USD | 1,940.00 USD | 0.00 USD | `+1.52%` | `15.31` |
| `Live` | `Short` | `129.50` | 37,620.00 USD | 33,080.00 USD | 0.00 USD | `+3.92%` | `255.45` |
| `Live` | `Short` | `130.50` | 208,310.00 USD | 170,680.00 USD | 0.00 USD | `+4.73%` | `1,307.91` |
| `Live` | `Short` | `131.50` | 208,580.00 USD | 269.57 USD | 0.00 USD | `+5.53%` | `2.05` |
| `Live` | `Short` | `132.50` | 221,010.00 USD | 12,430.00 USD | 0.00 USD | `+6.33%` | `93.82` |
| `Live` | `Short` | `133.50` | 236,380.00 USD | 15,370.00 USD | 0.00 USD | `+7.13%` | `115.15` |
| `Live` | `Short` | `136.50` | 318,000.00 USD | 81,620.00 USD | 0.00 USD | `+9.54%` | `597.95` |
| `Live` | `Short` | `137.50` | 320,850.00 USD | 2,850.00 USD | 0.00 USD | `+10.34%` | `20.75` |
| `Live` | `Short` | `138.50` | 323,700.00 USD | 2,850.00 USD | 0.00 USD | `+11.15%` | `20.56` |
| `Live` | `Short` | `139.50` | 323,800.00 USD | 100.44 USD | 0.00 USD | `+11.95%` | `0.72` |
| `Live` | `Short` | `140.50` | 324,950.00 USD | 1,150.00 USD | 0.00 USD | `+12.75%` | `8.19` |
| `Live` | `Short` | `141.50` | 348,860.00 USD | 23,900.00 USD | 0.00 USD | `+13.55%` | `168.93` |
| `Live` | `Short` | `142.50` | 351,380.00 USD | 2,530.00 USD | 0.00 USD | `+14.36%` | `17.73` |
| `Live` | `Short` | `143.50` | 365,010.00 USD | 13,630.00 USD | 0.00 USD | `+15.16%` | `95.00` |
| `Live` | `Short` | `144.50` | 929,460.00 USD | 564,450.00 USD | 0.00 USD | `+15.96%` | `3,906.20` |
| `Live` | `Short` | `146.50` | 930,190.00 USD | 732.50 USD | 0.00 USD | `+17.57%` | `5.00` |
| `Live` | `Short` | `150.50` | 930,360.00 USD | 167.06 USD | 0.00 USD | `+20.78%` | `1.11` |
| `Live` | `Short` | `151.50` | 942,940.00 USD | 12,580.00 USD | 0.00 USD | `+21.58%` | `83.02` |
| `Live` | `Short` | `154.50` | 4,500,000.00 USD | 3,550,000.00 USD | 0.00 USD | `+23.99%` | `23,000.00` |
| `Live` | `Short` | `155.50` | 4,500,000.00 USD | 2,200.00 USD | 0.00 USD | `+24.79%` | `14.13` |
| `Live` | `Short` | `158.50` | 4,500,000.00 USD | 1,480.00 USD | 0.00 USD | `+27.20%` | `9.36` |
| `Live` | `Short` | `162.50` | 4,500,000.00 USD | 160.88 USD | 0.00 USD | `+30.41%` | `0.99` |
| `Live` | `Short` | `166.50` | 4,550,000.00 USD | 51,920.00 USD | 0.00 USD | `+33.62%` | `311.81` |
| `Live` | `Short` | `167.50` | 4,560,000.00 USD | 12,770.00 USD | 0.00 USD | `+34.42%` | `76.26` |
| `Live` | `Short` | `168.50` | 4,570,000.00 USD | 4,360.00 USD | 0.00 USD | `+35.22%` | `25.90` |
| `Live` | `Short` | `171.50` | 4,570,000.00 USD | 1,060.00 USD | 0.00 USD | `+37.63%` | `6.20` |
| `Live` | `Short` | `172.50` | 4,570,000.00 USD | 1,550.00 USD | 0.00 USD | `+38.43%` | `9.00` |
| `Live` | `Short` | `173.50` | 4,570,000.00 USD | 202.99 USD | 0.00 USD | `+39.23%` | `1.17` |
| `Live` | `Short` | `175.50` | 4,580,000.00 USD | 5,620.00 USD | 0.00 USD | `+40.84%` | `32.04` |
| `Live` | `Short` | `179.50` | 4,580,000.00 USD | 387.72 USD | 0.00 USD | `+44.05%` | `2.16` |
| `Live` | `Short` | `180.50` | 4,890,000.00 USD | 315,860.00 USD | 0.00 USD | `+44.85%` | `1,749.91` |
| `Live` | `Short` | `181.50` | 4,900,000.00 USD | 2,170.00 USD | 0.00 USD | `+45.65%` | `11.93` |
| `Live` | `Short` | `183.50` | 4,900,000.00 USD | 141.30 USD | 0.00 USD | `+47.26%` | `0.77` |
| `Live` | `Short` | `184.50` | 4,930,000.00 USD | 34,110.00 USD | 0.00 USD | `+48.06%` | `184.90` |
| `Live` | `Short` | `186.50` | 4,930,000.00 USD | 1,890.00 USD | 0.00 USD | `+49.67%` | `10.15` |
| `Live` | `Short` | `187.50` | 4,930,000.00 USD | 2,330.00 USD | 0.00 USD | `+50.47%` | `12.41` |
| `Live` | `Short` | `189.50` | 4,930,000.00 USD | 295.62 USD | 0.00 USD | `+52.07%` | `1.56` |
| `Live` | `Short` | `194.50` | 4,950,000.00 USD | 16,590.00 USD | 0.00 USD | `+56.09%` | `85.28` |
| `Live` | `Short` | `195.50` | 4,990,000.00 USD | 40,040.00 USD | 0.00 USD | `+56.89%` | `204.83` |
| `Live` | `Short` | `196.50` | 8,330,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+57.69%` | `17,007.57` |
| `Live` | `Short` | `199.50` | 8,340,000.00 USD | 5,390.00 USD | 0.00 USD | `+60.10%` | `27.00` |
| `Live` | `Short` | `200.50` | 8,350,000.00 USD | 9,850.00 USD | 0.00 USD | `+60.90%` | `49.15` |
| `Live` | `Short` | `202.50` | 8,350,000.00 USD | 676.35 USD | 0.00 USD | `+62.51%` | `3.34` |
| `Live` | `Short` | `203.50` | 8,390,000.00 USD | 39,440.00 USD | 0.00 USD | `+63.31%` | `193.83` |
| `Live` | `Short` | `205.50` | 8,470,000.00 USD | 84,610.00 USD | 0.00 USD | `+64.91%` | `411.72` |
| `Live` | `Short` | `210.50` | 8,470,000.00 USD | 151.56 USD | 0.00 USD | `+68.93%` | `0.72` |
| `Live` | `Short` | `212.50` | 8,480,000.00 USD | 8,710.00 USD | 0.00 USD | `+70.53%` | `41.00` |
| `Live` | `Short` | `218.50` | 8,480,000.00 USD | 1,130.00 USD | 0.00 USD | `+75.35%` | `5.15` |
| `Live` | `Short` | `220.50` | 8,490,000.00 USD | 2,000.00 USD | 0.00 USD | `+76.95%` | `9.06` |
| `Live` | `Short` | `223.50` | 12,030,000.00 USD | 3,550,000.00 USD | 0.00 USD | `+79.36%` | `15,861.48` |
| `Live` | `Short` | `225.50` | 13,050,000.00 USD | 1,020,000.00 USD | 0.00 USD | `+80.96%` | `4,508.67` |
| `Live` | `Short` | `230.50` | 13,050,000.00 USD | 2,310.00 USD | 0.00 USD | `+84.98%` | `10.00` |
| `Live` | `Short` | `232.50` | 13,870,000.00 USD | 818,270.00 USD | 0.00 USD | `+86.58%` | `3,519.45` |
| `Live` | `Short` | `236.50` | 13,870,000.00 USD | 257.79 USD | 0.00 USD | `+89.79%` | `1.09` |
| `Live` | `Short` | `239.50` | 13,870,000.00 USD | 387.99 USD | 0.00 USD | `+92.20%` | `1.62` |
| `Live` | `Short` | `240.50` | 13,930,000.00 USD | 64,970.00 USD | 0.00 USD | `+93.00%` | `270.16` |

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
  * Current Rate: `-15.93K` | Last 24h: `15.72K` | Last 3d: `55.76K` | Last 7d: `119.40K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0041%` | **USDT OKX** | `-0.0004%` |
| **USDT Bybit** | `-0.0335%` | **USDT KuCoin** | `-0.0122%` |
| **USDT MEXC** | `0.0041%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0086%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `122.60` | `122.32` | `122.60` | `123.18` | `121.75` | 1,556,143.15 USD | 808,945.27 USD | 747,197.89 USD | 61,747.38 USD | `+3.97%` | `36B / 18S` |
| `0:00 UTC` | `123.50` | `123.59` | `123.50` | `124.12` | `122.77` | 1,930,466.83 USD | 1,169,577.61 USD | 760,889.22 USD | 408,688.38 USD | `+21.17%` | `33B / 9S` |
| `5:00 UTC` | `124.25` | `124.03` | `124.25` | `124.45` | `123.66` | 1,500,731.33 USD | 697,230.09 USD | 803,501.24 USD | -106,271.15 USD | `-7.08%` | `8B / 7S` |
| `0:00 UTC` | `123.52` | `123.26` | `123.52` | `123.91` | `122.69` | 2,022,565.96 USD | 1,006,456.45 USD | 1,016,109.51 USD | -9,653.06 USD | `-0.48%` | `17B / 14S` |
| `5:00 UTC` | `123.70` | `123.95` | `123.70` | `124.31` | `123.44` | 1,609,872.44 USD | 851,411.54 USD | 758,460.89 USD | 92,950.65 USD | `+5.77%` | `11B / 9S` |
| `0:00 UTC` | `124.56` | `124.51` | `124.56` | `124.78` | `124.06` | 1,620,060.54 USD | 772,586.85 USD | 847,473.69 USD | -74,886.85 USD | `-4.62%` | `14B / 15S` |
| `5:00 UTC` | `124.41` | `124.50` | `124.41` | `124.75` | `124.13` | 1,180,503.64 USD | 644,282.82 USD | 536,220.82 USD | 108,062.00 USD | `+9.15%` | `7B / 8S` |
| `0:00 UTC` | `124.66` | `125.75` | `124.66` | `127.18` | `124.34` | 2,947,595.56 USD | 1,739,301.93 USD | 1,208,293.63 USD | 531,008.30 USD | `+18.01%` | `27B / 7S` |
| `5:00 UTC` | `126.50` | `126.66` | `126.50` | `127.48` | `126.16` | 2,126,180.43 USD | 1,170,588.46 USD | 955,591.97 USD | 214,996.49 USD | `+10.11%` | `24B / 7S` |
| `0:00 UTC` | `126.53` | `126.49` | `126.53` | `126.84` | `126.18` | 1,134,159.92 USD | 513,895.05 USD | 620,264.87 USD | -106,369.82 USD | `-9.38%` | `6B / 23S` |

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
| `5m` | -18,760.00 USD | 241,290.00 USD | **`ACCUMULATION`** |
| `15m` | -180,440.00 USD | 479,620.00 USD | **`ACCUMULATION`** |
| `30m` | 299,540.00 USD | 2,310,000.00 USD | **`ACCUMULATION`** |
| `1h` | 461,030.00 USD | 3,110,000.00 USD | **`ACCUMULATION`** |
| `2h` | 354,730.00 USD | 3,400,000.00 USD | **`ACCUMULATION`** |
| `4h` | 686,180.00 USD | 5,650,000.00 USD | **`ACCUMULATION`** |
| `6h` | -658,460.00 USD | 3,690,000.00 USD | **`ACCUMULATION`** |
| `8h` | -1,910,000.00 USD | -7,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -6,060,000.00 USD | -7,900,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -6,720,000.00 USD | -8,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -28,410,000.00 USD | -47,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -116,640,000.00 USD | -103,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-18.76K` | 15m=`-180.44K` | 1h=`+461.03K` | 24h=`-6.72M`
* Futures Capital Netflows: 5m=`+241.29K` | 15m=`+479.62K` | 1h=`+3.11M` | 24h=`-8.37M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `115.55` (Risk Distance: `2.18` pts)
  * +2.5R Take Profit: `123.18`
  * Mathematical Lot Sizing: **`4.59 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `123.81` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `125.99` (Risk Distance: `2.18` pts)
  * +2.5R Take Profit: `118.36`
  * Mathematical Lot Sizing: **`4.59 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`127.53`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
